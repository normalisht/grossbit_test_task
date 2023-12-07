import io
import os
import uuid
from collections import Counter
from datetime import datetime
from pathlib import Path

import pdfkit
import qrcode
from django.conf import settings
from django.http import FileResponse
from django.shortcuts import render
from rest_framework.exceptions import ParseError
from rest_framework.viewsets import ViewSet

from .models import Item


class CashMachineViewSet(ViewSet):
    DATETIME_FORMAT = '%d.%m.%Y %H:%M'

    def create(self, request):
        item_ids = request.data.get('items')
        if not item_ids:
            raise ParseError(detail='Items cant be empty')

        template_data = self.get_template_data(item_ids=item_ids)
        template = render(
            request=request,
            template_name='cash_receipt.html',
            context=template_data
        ).content.decode('utf-8')

        Path(os.path.join(settings.MEDIA_ROOT)).mkdir(exist_ok=True)
        filename = f'{str(uuid.uuid4())}.pdf'
        pdfkit.from_string(
            template,
            output_path=os.path.join(settings.MEDIA_ROOT, filename),
            configuration=settings.PDFKIT_CONFIG
        )

        file_link = f'{settings.MEDIA_URL}{filename}'
        absolute_file_link = request.build_absolute_uri(file_link)
        qr_code = self.generate_qrcode(absolute_file_link)

        return FileResponse(
            qr_code,
            filename='cash_receipt_qrcode.png'
        )

    def get_template_data(self, item_ids: list[int]) -> dict:
        items = Item.objects.filter(id__in=item_ids)
        if not items:
            raise ParseError(detail='No items with this id')

        items_count = Counter(item_ids)

        items_data = []
        total = 0
        for item in items:
            item_cost = item.price * items_count.get(item.id)
            total += item_cost
            items_data.append({
                'name': item.name,
                'cost': item_cost,
                'amount': items_count.get(item.id)
            })

        return {
            'items': items_data,
            'total': total,
            'datetime': datetime.now().strftime(self.DATETIME_FORMAT),
        }

    @staticmethod
    def generate_qrcode(link):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=6,
            border=2,
        )
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        image_io = io.BytesIO()
        img.save(image_io, 'PNG')
        image_io.seek(0)

        return image_io

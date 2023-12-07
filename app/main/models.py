from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    price = models.PositiveIntegerField(verbose_name='Стоимость')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name}'

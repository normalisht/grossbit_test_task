from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CashMachineViewSet

router_v1 = DefaultRouter()
router_v1.register(
    'cache_machine',
    CashMachineViewSet,
    basename='cache_machine'
)

urlpatterns = [
    path('', include(router_v1.urls)),
]

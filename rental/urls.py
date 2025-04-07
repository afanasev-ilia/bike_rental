from django.urls import include, path
from rest_framework.routers import DefaultRouter

from rental.apps import RentalConfig
from rental.views import RentalCreateViewSet, RentalUpdateViewSet

app_name = RentalConfig.name

router = DefaultRouter()
router.register('start', RentalCreateViewSet, basename='start')
router.register('end', RentalUpdateViewSet, basename='end')

urlpatterns = [
    path('', include(router.urls)),
]

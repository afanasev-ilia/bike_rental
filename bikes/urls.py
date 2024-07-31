from django.urls import include, path
from rest_framework.routers import DefaultRouter

from bikes.apps import BikesConfig
from bikes.views import BikeListViewSet

app_name = BikesConfig.name


router = DefaultRouter()
router.register(
    '',
    BikeListViewSet,
    basename='bikes',
)

urlpatterns = [
    path('', include(router.urls)),
]

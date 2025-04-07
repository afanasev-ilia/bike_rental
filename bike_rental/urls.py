from django.contrib import admin
from django.urls import include, path

from bikes.apps import BikesConfig
from rental.apps import RentalConfig

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('users.urls'), name='users'),
    path('api/v1/bikes/', include('bikes.urls', namespace=BikesConfig.name)),
    path('api/v1/rental/', include('rental.urls', namespace=RentalConfig.name)),
]

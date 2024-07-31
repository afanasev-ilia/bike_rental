from django.db import models


class Bike(models.Model):
    bike_model = models.CharField(
        'модель велосипеда',
        max_length=50,
        unique=True,
        help_text='укажите модель велосипеда',
    )
    serial_number = models.CharField(
        'серийный номер',
        max_length=25,
        unique=True,
        help_text='укажите серийный номер',
    )
    is_rented = models.BooleanField(
        'статус аренды (арендован)',
        default=False,
        help_text='укажите статус аренды',
    )
    rental_price = models.FloatField(
        'cтоимость аренды в руб./час',
        help_text="укажите cтоимость аренды в руб./час",
    )

    class Meta:
        verbose_name = 'велосипед'
        verbose_name_plural = 'велосипеды'

    def __str__(self):
        return self.serial_number

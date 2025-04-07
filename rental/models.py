from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import UniqueConstraint, Q

from bikes.models import Bike

User = get_user_model()


class Rental(models.Model):
    renter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='rentals',
        verbose_name='арендатор',
        help_text='укажите арендатора',
    )
    bike = models.ForeignKey(
        Bike,
        on_delete=models.CASCADE,
        related_name='rentals',
        verbose_name='велосипед',
        help_text='укажите велосипед',
    )
    start_time = models.DateTimeField(
        'время начала аренды',
        auto_now_add=True,
        help_text='укажите время начала аренды'
    )
    end_time = models.DateTimeField(
        'время окончания аренды',
        blank=True,
        null=True,
        help_text='укажите время окончания аренды'
    )
    cost = models.FloatField(
        'стоимость',
        blank=True,
        null=True,
        help_text='стоимость аренды в рублях',
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['renter'],
                condition=Q(end_time=None),
                name='unique_active_rental',
            ),
        ]
        verbose_name = 'аренда'
        verbose_name_plural = 'аренды'

    def __str__(self):
        return f'Аренда велосипеда №{self.bike} пользователем {self.renter}'

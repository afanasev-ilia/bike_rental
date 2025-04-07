# Generated by Django 4.2.14 on 2024-07-31 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bikes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True, help_text='укажите время начала аренды', verbose_name='время начала аренды')),
                ('end_time', models.DateTimeField(blank=True, help_text='укажите время окончания аренды', null=True, verbose_name='время окончания аренды')),
                ('cost', models.FloatField(blank=True, help_text='стоимость аренды в рублях', null=True, verbose_name='стоимость')),
                ('bike', models.ForeignKey(help_text='укажите велосипед', on_delete=django.db.models.deletion.CASCADE, related_name='rentals', to='bikes.bike', verbose_name='велосипед')),
                ('renter', models.ForeignKey(help_text='укажите арендатора', on_delete=django.db.models.deletion.CASCADE, related_name='rentals', to=settings.AUTH_USER_MODEL, verbose_name='арендатор')),
            ],
            options={
                'verbose_name': 'аренда',
                'verbose_name_plural': 'аренды',
            },
        ),
        migrations.AddConstraint(
            model_name='rental',
            constraint=models.UniqueConstraint(condition=models.Q(('end_time', None)), fields=('renter',), name='unique_active_rental'),
        ),
    ]

# Generated by Django 4.2.14 on 2024-07-30 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(help_text='укажите серийный номер', max_length=25, unique=True, verbose_name='серийный номер')),
                ('is_rented', models.BooleanField(default=False, help_text='укажите статус аренды', verbose_name='статус аренды')),
                ('rental_price', models.FloatField(help_text='укажите cтоимость аренды в руб./час', verbose_name='cтоимость аренды в руб./час')),
            ],
            options={
                'verbose_name': 'велосипед',
                'verbose_name_plural': 'велосипеды',
            },
        ),
    ]

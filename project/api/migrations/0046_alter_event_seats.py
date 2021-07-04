# Generated by Django 3.2.3 on 2021-07-04 11:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0045_auto_20210704_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='seats',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество мест'),
        ),
    ]

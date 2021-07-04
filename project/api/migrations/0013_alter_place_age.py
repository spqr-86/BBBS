# Generated by Django 3.2.3 on 2021-06-09 13:31

from django.db import migrations, models

import api.validators


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20210609_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='age',
            field=models.SmallIntegerField(validators=[api.validators.age_validator], verbose_name='Возраст ребёнка'),
        ),
    ]

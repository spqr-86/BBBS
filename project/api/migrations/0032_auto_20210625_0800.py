# Generated by Django 3.2.3 on 2021-06-25 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_merge_20210624_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='image_url',
        ),
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='videos/'),
        ),
    ]

# Generated by Django 5.1.4 on 2024-12-24 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rehigh_app', '0004_rename_image_swiper_desktop_image_swiper_phone_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swiper',
            name='desktop_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

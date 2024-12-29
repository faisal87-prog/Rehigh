# Generated by Django 5.1.4 on 2024-12-24 16:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rehigh_app', '0003_appointment_car_model_appointment_createdat_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='swiper',
            old_name='image',
            new_name='desktop_image',
        ),
        migrations.AddField(
            model_name='swiper',
            name='phone_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('value', models.CharField(blank=True, max_length=200, null=True)),
                ('swiper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variations', to='rehigh_app.swiper')),
            ],
        ),
    ]

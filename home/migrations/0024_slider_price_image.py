# Generated by Django 4.0.6 on 2022-07-16 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_remove_slider_status_slider_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='price_image',
            field=models.ImageField(blank=True, default='slider/not_found_slider.png', upload_to='slider/%y/%m/%d/'),
        ),
    ]

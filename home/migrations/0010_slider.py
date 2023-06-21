# Generated by Django 4.0.5 on 2022-07-09 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_settings_dribbble_settings_googleplus_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('sub_title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('image', models.ImageField(blank=True, default='slider/not_found_slider.png', upload_to='slider/%y/%m/%d/')),
                ('status', models.CharField(choices=[('true', 'Açık'), ('false', 'Kapalı')], max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
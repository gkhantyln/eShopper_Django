# Generated by Django 4.0.5 on 2022-07-10 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='worktime',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
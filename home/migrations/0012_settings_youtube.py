# Generated by Django 4.0.5 on 2022-07-10 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_settings_worktime'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='youtube',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
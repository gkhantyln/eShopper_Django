# Generated by Django 4.0.5 on 2022-07-08 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rename_desightext_settings_designlink_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='fimaptext',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='settings',
            name='finfotext',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

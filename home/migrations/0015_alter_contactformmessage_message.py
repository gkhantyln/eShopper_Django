# Generated by Django 4.0.5 on 2022-07-10 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_contactformmessage_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformmessage',
            name='message',
            field=models.TextField(max_length=255),
        ),
    ]

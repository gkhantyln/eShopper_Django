# Generated by Django 4.0.6 on 2022-07-11 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_blogs_author_blogs_create_at_blogs_update_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]

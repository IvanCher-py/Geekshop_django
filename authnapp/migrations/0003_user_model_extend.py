# Generated by Django 2.2.17 on 2021-03-13 08:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0002_user_model_extend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 15, 8, 12, 37, 801742, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]

# Generated by Django 2.1.1 on 2018-09-29 14:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20180927_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='create_date_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
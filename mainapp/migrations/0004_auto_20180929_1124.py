# Generated by Django 2.1.1 on 2018-09-29 14:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20180929_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='create_date_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Data do Lançamento'),
        ),
        migrations.AlterField(
            model_name='records',
            name='db_included_date_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Inclusão no Bando de Dados'),
        ),
        migrations.AlterField(
            model_name='records',
            name='payment_date_time',
            field=models.DateTimeField(default=datetime.datetime.now, null=True, verbose_name='Data da Execução'),
        ),
    ]
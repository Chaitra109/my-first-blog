# Generated by Django 3.1.7 on 2021-04-17 11:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 17, 11, 50, 27, 577034, tzinfo=utc)),
        ),
    ]

# Generated by Django 2.2.6 on 2019-11-23 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTable', '0006_auto_20191123_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='pub_date',
            field=models.DateField(verbose_name='date published'),
        ),
    ]
# Generated by Django 2.2.6 on 2019-11-28 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTable', '0009_auto_20191127_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='img',
            field=models.ImageField(upload_to='img/'),
        ),
    ]
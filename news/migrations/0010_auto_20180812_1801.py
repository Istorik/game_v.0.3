# Generated by Django 2.1 on 2018-08-12 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20180812_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='id_item',
            field=models.CharField(max_length=64),
        ),
    ]
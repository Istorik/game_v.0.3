# Generated by Django 2.1 on 2018-08-12 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20180812_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_owne', models.IntegerField(default=0)),
                ('id_item', models.CharField(max_length=64, verbose_name='Название')),
                ('slot', models.IntegerField(default=9)),
            ],
            options={
                'verbose_name': 'База Предметов',
                'verbose_name_plural': 'База Предметов',
            },
        ),
    ]

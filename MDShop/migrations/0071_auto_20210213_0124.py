# Generated by Django 3.1.4 on 2021-02-12 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MDShop', '0070_auto_20210213_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.PositiveSmallIntegerField(blank='2', verbose_name='цена'),
        ),
    ]

# Generated by Django 3.1.1 on 2020-12-04 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MDShop', '0012_auto_20201205_0041'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartphone',
            name='razdel',
            field=models.ManyToManyField(to='MDShop.Razdel', verbose_name='Категория'),
        ),
    ]
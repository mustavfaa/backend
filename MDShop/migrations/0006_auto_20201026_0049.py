# Generated by Django 3.1.1 on 2020-10-25 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MDShop', '0005_auto_20201026_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]

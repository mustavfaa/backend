# Generated by Django 3.1.4 on 2021-01-21 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MDShop', '0032_auto_20210122_0147'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='like',
            options={'ordering': ['likefov']},
        ),
        migrations.AlterField(
            model_name='customer',
            name='likecus',
            field=models.ManyToManyField(blank=True, null=True, to='MDShop.like', verbose_name='лайк'),
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-25 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_alter_shoe_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='price',
            field=models.IntegerField(max_length=20),
        ),
    ]

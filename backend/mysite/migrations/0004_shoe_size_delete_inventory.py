# Generated by Django 5.0.4 on 2024-04-25 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_alter_category_description_alter_shoe_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='size',
            field=models.JSONField(null=True),
        ),
        migrations.DeleteModel(
            name='Inventory',
        ),
    ]

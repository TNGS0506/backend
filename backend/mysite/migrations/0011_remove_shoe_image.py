# Generated by Django 5.0.4 on 2024-05-14 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0010_alter_size_shoe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoe',
            name='image',
        ),
    ]

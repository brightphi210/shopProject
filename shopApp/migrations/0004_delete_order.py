# Generated by Django 5.0.6 on 2024-06-06 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0003_delete_usermodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]

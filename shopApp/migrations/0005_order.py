# Generated by Django 5.0.6 on 2024-06-06 09:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0004_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shopApp.customer')),
                ('orderItem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shopApp.orderitem')),
            ],
        ),
    ]

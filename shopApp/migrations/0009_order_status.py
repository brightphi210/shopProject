# Generated by Django 5.0.6 on 2024-06-06 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0008_remove_order_issuccessful'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('PENDING', 'PENDING'), ('PROCESSING', 'PROCESSING'), ('DELIVERED', 'DELIVERED'), ('CANCELLED', 'CANCELLED')], max_length=255, null=True),
        ),
    ]

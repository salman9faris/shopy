# Generated by Django 5.0.6 on 2024-07-11 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_shippingcharge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingcharge',
            name='minimum_amount',
            field=models.CharField(default=0, max_length=24),
        ),
        migrations.AlterField(
            model_name='shippingcharge',
            name='shipping_charge',
            field=models.CharField(default=0, max_length=24),
        ),
    ]

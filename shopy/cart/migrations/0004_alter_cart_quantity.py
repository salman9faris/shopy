# Generated by Django 5.0.6 on 2024-07-12 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_rename_customer_name_cart_user_alter_cart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]

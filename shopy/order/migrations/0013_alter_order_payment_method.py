# Generated by Django 5.0.6 on 2024-07-11 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_alter_shippingaddress_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Payment_method',
            field=models.CharField(choices=[('COD', 'COD'), ('Debit/Credit card', 'Debit/Credit card'), ('Net banking', 'Net banking')], max_length=80),
        ),
    ]

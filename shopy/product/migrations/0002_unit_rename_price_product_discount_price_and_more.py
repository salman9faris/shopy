# Generated by Django 5.0.6 on 2024-07-13 18:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('unit', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='discount_price',
        ),
        migrations.AddField(
            model_name='product',
            name='disount_percentage',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, max_length=400, upload_to='product'),
        ),
        migrations.AddField(
            model_name='product',
            name='orginal_price',
            field=models.CharField(default=23, max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.ForeignKey(max_length=256, on_delete=django.db.models.deletion.CASCADE, to='product.unit'),
        ),
    ]
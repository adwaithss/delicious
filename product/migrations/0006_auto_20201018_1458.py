# Generated by Django 3.1.1 on 2020-10-18 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='specialPrice',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='product',
            name='total',
            field=models.FloatField(default=0.0),
        ),
    ]
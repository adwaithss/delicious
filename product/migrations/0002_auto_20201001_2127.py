# Generated by Django 3.1.1 on 2020-10-01 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(default=1, upload_to='product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(null=True, upload_to='product'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(null=True, upload_to='product'),
        ),
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(null=True, upload_to='product'),
        ),
    ]
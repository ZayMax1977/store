# Generated by Django 3.2.13 on 2023-04-07 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='photo/%Y/%m/%d/'),
        ),
    ]

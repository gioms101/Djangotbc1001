# Generated by Django 5.0.7 on 2024-10-10 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default=None, upload_to='products/'),
        ),
    ]

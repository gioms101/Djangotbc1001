# Generated by Django 5.0.7 on 2024-10-10 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, to='store.category'),
        ),
    ]
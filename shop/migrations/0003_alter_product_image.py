# Generated by Django 5.1.3 on 2025-01-08 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_id_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='core/static/products/images/'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-02 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='photo',
        ),
    ]

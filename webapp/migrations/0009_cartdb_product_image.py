# Generated by Django 5.1.1 on 2024-11-19 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_alter_checkoutdb_mobilenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdb',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='Cart Images'),
        ),
    ]

# Generated by Django 5.1.1 on 2024-11-14 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_cartdb_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkoutDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('Companyname', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('emailaddress', models.CharField(blank=True, max_length=100, null=True)),
                ('mobilenumber', models.IntegerField(blank=True, null=True)),
                ('Totalprice', models.IntegerField(blank=True, null=True)),
                ('message', models.TextField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
# Generated by Django 2.2.9 on 2020-01-08 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='test1',
            field=models.GenericIPAddressField(blank=True, null=True, protocol='IPv4'),
        ),
    ]

# Generated by Django 2.2.9 on 2020-01-14 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_auto_20200108_0827"),
    ]

    operations = [
        migrations.AddField(
            model_name="customtext",
            name="test",
            field=models.GenericIPAddressField(blank=True, null=True, protocol="IPv4"),
        ),
    ]

# Generated by Django 4.1 on 2022-08-29 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("oc_lettings_site", "0002_alter_address_options"),
        ("lettings", "0002_auto_20220829_1753"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="letting",
            name="address",
        ),
        migrations.DeleteModel(
            name="Address",
        ),
        migrations.DeleteModel(
            name="Letting",
        ),
    ]

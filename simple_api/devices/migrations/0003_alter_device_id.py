# Generated by Django 4.0.4 on 2022-05-17 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("devices", "0002_alter_device_note"),
    ]

    operations = [
        migrations.AlterField(
            model_name="device",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

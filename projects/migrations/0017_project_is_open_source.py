# Generated by Django 3.0.6 on 2020-05-22 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0016_auto_20200515_1210"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="is_open_source",
            field=models.BooleanField(default=False),
        ),
    ]

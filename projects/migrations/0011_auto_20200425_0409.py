# Generated by Django 3.0.5 on 2020-04-25 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0010_auto_20200316_2311"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project", name="slug", field=models.SlugField(),
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-25 17:59

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0011_auto_20200425_0409"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                editable=False, populate_from="website_title"
            ),
        ),
    ]

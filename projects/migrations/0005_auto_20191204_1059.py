# Generated by Django 3.0 on 2019-12-04 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20191204_1058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='draft',
        ),
        migrations.AddField(
            model_name='project',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
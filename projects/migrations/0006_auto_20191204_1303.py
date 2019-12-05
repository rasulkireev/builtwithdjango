# Generated by Django 3.0 on 2019-12-04 18:03

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('projects', '0005_auto_20191204_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='project',
            name='website_github',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='website_twitter',
            field=models.URLField(blank=True),
        ),
    ]
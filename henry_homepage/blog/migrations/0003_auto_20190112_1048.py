# Generated by Django 2.1.5 on 2019-01-12 10:48

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('blog', '0002_remove_post_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='Henry Yang', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='post_logo',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
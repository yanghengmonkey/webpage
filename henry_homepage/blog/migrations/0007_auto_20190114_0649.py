# Generated by Django 2.1.5 on 2019-01-14 06:49

from django.db import migrations
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190114_0618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=martor.models.MartorField(),
        ),
    ]
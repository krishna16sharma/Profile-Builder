# Generated by Django 3.0.5 on 2021-06-02 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_builder', '0008_auto_20210602_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='title',
        ),
    ]

# Generated by Django 3.0.5 on 2021-06-02 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_builder', '0006_auto_20210502_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin_data',
            name='username',
            field=models.TextField(default='admin1'),
        ),
    ]
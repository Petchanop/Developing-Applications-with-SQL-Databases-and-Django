# Generated by Django 3.1.3 on 2021-09-18 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0015_auto_20210917_2139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='choices',
        ),
    ]

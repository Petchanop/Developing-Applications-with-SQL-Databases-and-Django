# Generated by Django 3.1.3 on 2021-09-16 16:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0008_auto_20210916_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='date_submitted',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

# Generated by Django 3.1.3 on 2021-09-18 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0021_remove_choice_lesson'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='choice_submitted',
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_submitted',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='onlinecourse.submission'),
        ),
    ]

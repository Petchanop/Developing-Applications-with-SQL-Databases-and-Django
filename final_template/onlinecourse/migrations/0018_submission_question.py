# Generated by Django 3.1.3 on 2021-09-18 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0017_remove_submission_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='onlinecourse.question'),
        ),
    ]

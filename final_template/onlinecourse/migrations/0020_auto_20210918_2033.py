# Generated by Django 3.1.3 on 2021-09-18 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0019_auto_20210918_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='choice',
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_submitted',
            field=models.ManyToManyField(related_name='submitted', through='onlinecourse.Submission', to='onlinecourse.Lesson'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='onlinecourse.question'),
        ),
        migrations.AddField(
            model_name='submission',
            name='choice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='onlinecourse.choice'),
        ),
        migrations.AddField(
            model_name='submission',
            name='lesson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='onlinecourse.lesson'),
        ),
    ]

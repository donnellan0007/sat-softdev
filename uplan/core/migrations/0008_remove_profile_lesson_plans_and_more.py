# Generated by Django 4.1.3 on 2023-07-18 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_subject_lessonplan_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='lesson_plans',
        ),
        migrations.AlterField(
            model_name='lessonplan',
            name='primary_teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lessons', to='core.profile'),
        ),
    ]

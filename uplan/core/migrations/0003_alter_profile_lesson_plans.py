# Generated by Django 4.1.3 on 2023-06-14 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_profile_lesson_plans_profile_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='lesson_plans',
            field=models.ManyToManyField(blank=True, null=True, related_name='lesson_plan', to='core.lessonplan'),
        ),
    ]

# Generated by Django 4.1 on 2023-07-20 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_lessonplan_subject_lessonplan_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonplan',
            name='subject',
            field=models.ManyToManyField(blank=True, to='core.subject'),
        ),
    ]

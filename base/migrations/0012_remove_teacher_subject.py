# Generated by Django 4.2 on 2023-04-20 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_teacher_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='subject',
        ),
    ]

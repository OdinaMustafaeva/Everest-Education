# Generated by Django 4.2 on 2023-04-17 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
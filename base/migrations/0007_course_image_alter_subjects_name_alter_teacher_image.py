# Generated by Django 4.2 on 2023-04-20 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_ielts_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default='4317_Y7xt2pm.jpg', upload_to='media'),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default='avatr.svg', upload_to=''),
        ),
    ]

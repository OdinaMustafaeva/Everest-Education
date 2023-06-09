# Generated by Django 4.2 on 2023-04-20 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_textbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='ielts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ielts', models.FloatField(max_length=9.0)),
                ('image', models.ImageField(upload_to='')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_stu_ielts', to='base.teacher')),
            ],
        ),
        migrations.DeleteModel(
            name='textbook',
        ),
    ]

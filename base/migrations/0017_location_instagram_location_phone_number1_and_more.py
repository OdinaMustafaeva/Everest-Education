# Generated by Django 4.2 on 2023-04-26 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0016_profile_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='instagram',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='phone_number1',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='phone_number2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='telegram',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='contact',
        ),
    ]
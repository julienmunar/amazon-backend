# Generated by Django 4.0.5 on 2022-06-30 12:02

from django.db import migrations, models
import myUser.models


class Migration(migrations.Migration):

    dependencies = [
        ('myUser', '0002_alter_myuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=myUser.models.user_directory_path),
        ),
    ]
# Generated by Django 5.0.4 on 2024-04-29 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflixapp', '0002_alter_video_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(max_length=1000000, upload_to='movies'),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]
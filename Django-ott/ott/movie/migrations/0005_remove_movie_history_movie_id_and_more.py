# Generated by Django 5.0.7 on 2024-10-27 14:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_alter_movie_thumbnail_alter_movie_video'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie_history',
            name='movie_id',
        ),
        migrations.RemoveField(
            model_name='movie_history',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='watch_list',
            name='movie_id',
        ),
        migrations.RemoveField(
            model_name='watch_list',
            name='user_id',
        ),
        migrations.AddField(
            model_name='movie_history',
            name='movie_id',
            field=models.ManyToManyField(to='movie.movie'),
        ),
        migrations.AddField(
            model_name='movie_history',
            name='user_id',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='watch_list',
            name='movie_id',
            field=models.ManyToManyField(to='movie.movie'),
        ),
        migrations.AddField(
            model_name='watch_list',
            name='user_id',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]

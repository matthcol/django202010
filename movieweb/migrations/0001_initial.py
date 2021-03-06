# Generated by Django 3.1.2 on 2020-10-28 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('year', models.SmallIntegerField()),
                ('duration', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'movies',
            },
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('birthdate', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'stars',
            },
        ),
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=100)),
                ('actor', models.ForeignKey(db_column='id_actor', on_delete=django.db.models.deletion.CASCADE, to='movieweb.star')),
                ('movie', models.ForeignKey(db_column='id_movie', on_delete=django.db.models.deletion.CASCADE, to='movieweb.movie')),
            ],
            options={
                'db_table': 'play3',
            },
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='playedMovies', through='movieweb.Play', to='movieweb.Star'),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(blank=True, db_column='id_director', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='directedMovies', to='movieweb.star'),
        ),
    ]

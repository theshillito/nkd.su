# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import nkdsu.apps.vote.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reason', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(nkdsu.apps.vote.models.CleanOnSaveMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Discard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(nkdsu.apps.vote.models.CleanOnSaveMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('public', models.BooleanField(default=False)),
                ('content', models.TextField()),
            ],
            options={
            },
            bases=(nkdsu.apps.vote.models.CleanOnSaveMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(db_index=True)),
                ('tweet_id', models.BigIntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(nkdsu.apps.vote.models.SetShowBasedOnDateMixin, nkdsu.apps.vote.models.CleanOnSaveMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('successful', models.BooleanField(default=False)),
                ('blob', models.TextField()),
            ],
            options={
            },
            bases=(nkdsu.apps.vote.models.CleanOnSaveMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Shortlist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('index', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-show__showtime', 'index'],
            },
            bases=(nkdsu.apps.vote.models.CleanOnSaveMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('showtime', models.DateTimeField(db_index=True)),
                ('end', models.DateTimeField(db_index=True)),
            ],
            options={
            },
            bases=(nkdsu.apps.vote.models.CleanOnSaveMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.CharField(max_length=16, serialize=False, primary_key=True)),
                ('id3_title', models.CharField(max_length=500)),
                ('id3_artist', models.CharField(max_length=500)),
                ('id3_album', models.CharField(max_length=500, blank=True)),
                ('msec', models.IntegerField(null=True, blank=True)),
                ('added', models.DateTimeField()),
                ('revealed', models.DateTimeField(db_index=True, null=True, blank=True)),
                ('hidden', models.BooleanField(default=False)),
                ('inudesu', models.BooleanField(default=False)),
                ('background_art', models.ImageField(upload_to=nkdsu.apps.vote.models.art_filename, blank=True)),
            ],
            options={
            },
            bases=(nkdsu.apps.vote.models.CleanOnSaveMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TwitterUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('screen_name', models.CharField(max_length=100)),
                ('user_id', models.BigIntegerField(unique=True)),
                ('user_image', models.URLField()),
                ('name', models.CharField(max_length=20)),
                ('is_abuser', models.BooleanField(default=False)),
                ('updated', models.DateTimeField()),
            ],
            options={
            },
            bases=(nkdsu.apps.vote.models.CleanOnSaveMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(db_index=True)),
                ('text', models.TextField(blank=True)),
                ('tweet_id', models.BigIntegerField(null=True, blank=True)),
                ('name', models.CharField(max_length=40, blank=True)),
                ('kind', models.CharField(blank=True, max_length=10, choices=[(b'email', b'email'), (b'text', b'text'), (b'tweet', b'tweet')])),
                ('show', models.ForeignKey(related_name=b'vote_set', to='vote.Show')),
                ('tracks', models.ManyToManyField(to='vote.Track', db_index=True)),
                ('twitter_user', models.ForeignKey(blank=True, to='vote.TwitterUser', null=True)),
            ],
            options={
            },
            bases=(nkdsu.apps.vote.models.SetShowBasedOnDateMixin, nkdsu.apps.vote.models.CleanOnSaveMixin, models.Model),
        ),
        migrations.AddField(
            model_name='shortlist',
            name='show',
            field=models.ForeignKey(to='vote.Show'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shortlist',
            name='track',
            field=models.ForeignKey(to='vote.Track'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='shortlist',
            unique_together=set([('show', 'track'), ('show', 'index')]),
        ),
        migrations.AddField(
            model_name='play',
            name='show',
            field=models.ForeignKey(to='vote.Show'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='play',
            name='track',
            field=models.ForeignKey(to='vote.Track'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='note',
            name='show',
            field=models.ForeignKey(blank=True, to='vote.Show', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='note',
            name='track',
            field=models.ForeignKey(to='vote.Track'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='discard',
            name='show',
            field=models.ForeignKey(to='vote.Show'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='discard',
            name='track',
            field=models.ForeignKey(to='vote.Track'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='discard',
            unique_together=set([('show', 'track')]),
        ),
        migrations.AddField(
            model_name='block',
            name='show',
            field=models.ForeignKey(to='vote.Show'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='block',
            name='track',
            field=models.ForeignKey(to='vote.Track'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='block',
            unique_together=set([('show', 'track')]),
        ),
    ]

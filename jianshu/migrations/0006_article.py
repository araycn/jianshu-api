# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-27 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jianshu', '0005_auto_20160727_0905'),
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('article_id', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name=b'ID')),
                ('article_url', models.URLField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0URL')),
                ('article_user', models.CharField(max_length=100, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85')),
                ('article_user_url', models.URLField(verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85URL')),
                ('article_image', models.URLField(verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87URL')),
                ('article_title', models.CharField(max_length=100, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\xa0\x87\xe9\xa2\x98')),
                ('article_body', models.TextField(null=True, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x86\x85\xe5\xae\xb9')),
                ('article_time', models.CharField(max_length=100, null=True, verbose_name=b'\xe5\x8f\x91\xe8\xa1\xa8\xe6\x97\xb6\xe9\x97\xb4')),
                ('article_views_count', models.CharField(max_length=100, verbose_name=b'\xe9\x98\x85\xe8\xaf\xbb\xe6\x95\xb0')),
                ('public_comments_count', models.CharField(max_length=100, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe6\x95\xb0')),
                ('article_likes_count', models.CharField(max_length=100, verbose_name=b'\xe5\x96\x9c\xe6\xac\xa2')),
                ('total_rewards_count', models.CharField(max_length=100, verbose_name=b'\xe6\x89\x93\xe8\xb5\x8f')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='AnswerLike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('likeType', models.IntegerField(default=0)),
                ('answer', models.ForeignKey(to='ask.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.ImageField(upload_to=b'/upload/')),
                ('rating', models.IntegerField(default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('rating', models.IntegerField(default=0, db_index=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionLike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('likeType', models.IntegerField(default=0)),
                ('question', models.ForeignKey(to='ask.Question')),
                ('user_ptr', models.ForeignKey(to='ask.CustomUser')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='ask.Tag'),
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(to='ask.CustomUser'),
        ),
        migrations.AddField(
            model_name='answerlike',
            name='user_ptr',
            field=models.ForeignKey(to='ask.CustomUser'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='ask.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(to='ask.CustomUser'),
        ),
        migrations.AlterUniqueTogether(
            name='questionlike',
            unique_together=set([('user_ptr', 'question')]),
        ),
        migrations.AlterUniqueTogether(
            name='answerlike',
            unique_together=set([('user_ptr', 'answer')]),
        ),
    ]

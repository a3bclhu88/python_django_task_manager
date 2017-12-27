# Generated by Django 2.0 on 2017-12-20 04:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasktype', models.CharField(max_length=20)),
                ('taskname', models.CharField(max_length=40)),
                ('taskstarttime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('taskprogress', models.FloatField(default=0.0)),
                ('taskcurrentstage', models.CharField(max_length=20)),
                ('taskstatus', models.CharField(max_length=20)),
            ],
        ),
    ]

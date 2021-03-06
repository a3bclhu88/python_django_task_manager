# Generated by Django 2.0 on 2018-01-05 20:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20171227_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actionname', models.CharField(max_length=256)),
                ('actiontime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('actiontype', models.CharField(max_length=32)),
                ('Taskid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Task')),
            ],
        ),
    ]

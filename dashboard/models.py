from django.db import models
from datetime import datetime

from unittest.util import _MAX_LENGTH
import logging
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class TaskType(models.Model):
    tasktypename = models.CharField(max_length=20)
    def __str__(self):
        return self.tasktypename
    
class returncode(models.Model):
    returncodetype = models.CharField(max_length=20)
    returncodevalue = models.CharField(max_length=20)
    def __str__(self):
        return self.returncodevalue
    
class executable(models.Model):
    binarypath =  models.CharField(max_length=256,null='Ture')
    binaryhost = models.CharField(max_length=256,null='Ture')
    healthcheckpath = models.CharField(max_length=256,null='Ture')
    codesuccess = models.ForeignKey(returncode,on_delete=models.CASCADE,related_name='success_code',null='Ture')
    codefailure = models.ForeignKey(returncode,on_delete=models.CASCADE,related_name='fail_code',null='Ture')
    def __str__(self):
        return self.binarypath
    
class taskcurrentstage(models.Model):
    stagename = models.CharField(max_length=20)
    stageprogram = models.ForeignKey(executable,on_delete=models.CASCADE,null='Ture')
    def __str__(self):
        return self.stagename

class taskstatus(models.Model):
    statusname = models.CharField(max_length=20)
    def __str__(self):
        return self.statusname

class Task(models.Model):
    # field definition
    defaultindex = 1
    tasktype = models.ForeignKey(TaskType,on_delete=models.CASCADE,)
    taskname = models.CharField(max_length=20)
    taskstarttime = models.DateTimeField(default=datetime.now,blank = True)
    taskendtime = models.DateTimeField(null=True)
    taskprogress = models.FloatField(default=0.0)
    taskcurrentstage = models.ForeignKey(taskcurrentstage,on_delete=models.CASCADE,default = defaultindex)
    taskstatus = models.ForeignKey(taskstatus,on_delete=models.CASCADE,default = defaultindex)
    def __str__(self):
        return self.taskname



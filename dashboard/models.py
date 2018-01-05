from django.db import models
from datetime import datetime

from unittest.util import _MAX_LENGTH
import logging
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# type of the task, file onboarding, file check, etc
class TaskType(models.Model):
    tasktypename = models.CharField(max_length=20)
    def __str__(self):
        return self.tasktypename

# list of return code of executed program     
class returncode(models.Model):
    returncodetype = models.CharField(max_length=20)
    returncodevalue = models.CharField(max_length=20)
    def __str__(self):
        return self.returncodevalue

#status behavior , pre-execut, execute, success, failure
class statusbehavior(models.Model):
    statusbehavior = models.CharField(max_length=20,default='to-be-execute')
    def __str__(self):
        return self.statusbehavior

# information of executable binaries tied to each execution stage of a task   
class executable(models.Model):
    binarypath =  models.CharField(max_length=256,null='Ture')
    binaryhost = models.CharField(max_length=256,null='Ture')
    healthcheckpath = models.CharField(max_length=256,null='Ture')
    codesuccess = models.ForeignKey(returncode,on_delete=models.CASCADE,related_name='success_code',null='Ture')
    codefailure = models.ForeignKey(returncode,on_delete=models.CASCADE,related_name='fail_code',null='Ture')
    def __str__(self):
        return self.binarypath

# stages of a task if it contains more than one   
class taskcurrentstage(models.Model):
    stagename = models.CharField(max_length=20)
    stageprogram = models.ForeignKey(executable,on_delete=models.CASCADE,null='Ture')
    def __str__(self):
        return self.stagename

#status of a task, scheduled, running, success, failure
class taskstatus(models.Model):
    statusname = models.CharField(max_length=20)
    statusbehavior = models.ForeignKey(statusbehavior,on_delete=models.CASCADE,null=True)
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

class TaskAction(models.Model):
    # task action item
    Taskid = models.ForeignKey(Task,on_delete=models.CASCADE, null=True)
    actionname = models.CharField(max_length = 256)
    actiontime = models.DateTimeField(default = datetime.now,blank = True)
    actiontype = models.CharField(max_length = 32)

'''
Created on Dec 23, 2017

@author: Andy
'''
from dashboard.models import Task
import logging
from django.db.models.signals import post_save
from django.dispatch import receiver

logger = logging.getLogger(__name__)

#@receiver(post_save,sender=Task)
def task_initiation(sender,instance,created):
   # if created:
        import sys
        print>>sys.stdout('[sys out print] : task '+instance.taskname+' is created and initialized to stage '+instance.taskcurrentstage)
        instance.taskname =  instance.taskname + 'av'
#def task_deletion(sender,instance,created,**kwargs):
#    logger.info('[sys out print] : task '+instance.taskname+' is deleted)
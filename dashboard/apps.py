from django.apps import AppConfig
from django.db.models.signals import post_save, pre_init
from dashboard.signals import task_initiation
from dashboard.models import Task


class DashboardConfig(AppConfig):
    name = 'dashboard'
    def ready(self):
#        from dashboard.models import Task
#        import dashboard.signals.task_initiation
 #       pre_init.connect(task_initiation, sender='dashboard.Task')
from django.contrib import admin
from dashboard.models import Task
from django.forms import ModelChoiceField
from django.forms import ModelForm
from dashboard.models import TaskType
from dashboard.models import taskstatus
from dashboard.models import taskcurrentstage
from dashboard.models import returncode
from dashboard.models import executable


# Register your models here.
#admin.site.register(Task)

#class taskTypedropdown (ModelChoiceField):
#    def label_from_instance(self, obj):
#        return obj.tasktypename()

class taskCreationForm (ModelForm):
    #tasktype = taskTypedropdown(TaskType.objects.all())
    class Meta:
        model = Task
        exclude = ['taskendtime', 'taskcurrentstage','taskstatus']
    
class customedTask (admin.ModelAdmin):
    exclude = ['taskendtime', 'taskcurrentstage','taskstatus']
    form = taskCreationForm
    class Meta:
        model = Task
    
admin.site.register(Task,customedTask)
admin.site.register(taskstatus)
admin.site.register(TaskType)
admin.site.register(taskcurrentstage)
admin.site.register(returncode)
admin.site.register(executable)

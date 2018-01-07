from django.shortcuts import render
from .models import Task
from django.template.context_processors import request
from lib2to3.fixes.fix_input import context
from .models import TaskAction
from dashboard.models import TaskAction

# Create your views here.

def index(request):
    
    tasklist = Task.objects.all()
    
    
    context = {
            'tastlisttitle':'list of task created',
            'tasklist':tasklist
        }
    
    return render(request,'index.html',context)

#def taskcreation(request):
    
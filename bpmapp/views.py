from django.shortcuts import render

def home(request):
    return render(request,'bpmapp/__base.html',{})
    

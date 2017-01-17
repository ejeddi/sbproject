from django.shortcuts import render

def home(request):
    return render(request,'bpmapp/__base.html',{})
    
def process_new(request):
    return render(request,'bpmapp/process_new.html',{})

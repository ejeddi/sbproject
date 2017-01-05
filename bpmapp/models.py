from django.db import models
from django.utils import timezone

class Project(models.Model):
    name=models.CharField(max_length=50, unique=True,blank=False)
    desc=models.TextField(max_length=1000,blank=True,)
    def __str__(self):
        return self.name

class ProcessType(models.Model):
    name=models.CharField(max_length=20, unique=True,)
    
    def __str__(self):
            return self.name
        
class ProdLine(models.Model):
    name=models.CharField(max_length=30, unique=True,)
    
    def __str__(self):
        return self.name
    
class Business(models.Model):
    name=models.CharField(max_length=30, unique=True,)
    
    class Meta:
        verbose_name_plural = 'Businesses'
    
    def __str__(self):
        return self.name
    
class Status(models.Model):
    name=models.CharField(max_length=20, unique=True,)
    
    class Meta:
        verbose_name_plural = 'Statuses'
        
    def __str__(self):
        return self.name
    
class Activity(models.Model):
    name=models.CharField(max_length=30,unique=True,)

    class Meta:
        verbose_name_plural = 'Activities'
        
    def __str__(self):
        return self.name
    
class Action(models.Model):
    name=models.CharField(max_length=30, unique=True,)

    def __str__(self):
        return self.name
    
class ProcessBluePrint(models.Model):
    name=models.CharField(max_length=50, unique=True,)
    desc=models.CharField(max_length=255,)

    def __str__(self):
        return self.name

class ActivityBluePrint(models.Model):
    tag=models.CharField(max_length=10,)
    caption=models.CharField(max_length=50,blank=True)
    process_BluePrint=models.ForeignKey('ProcessBluePrint')
    activity=models.ForeignKey('Activity')
    action=models.ForeignKey('Action')
    actor=models.ForeignKey('auth.User')

class FlowBluePrint(models.Model):
    caption=models.CharField(max_length=50,blank=True)
    process_Blueprint=models.ForeignKey('ProcessBluePrint')
    origin=models.ForeignKey('ActivityBluePrint',related_name='origin')
    destination=models.ForeignKey('ActivityBluePrint',related_name='destination')
    
class Process(ProcessBluePrint, models.Model):
    type=models.ForeignKey('ProcessType')
    prodline=models.ForeignKey('ProdLine')
    business=models.ForeignKey('Business')
    project=models.ForeignKey('Project')
    start=models.DateTimeField(auto_now_add=True,)
    #end=models.DateTimeField(blank=True, auto_now=True)
    user_created=models.ForeignKey('auth.User')
    date_created=models.DateTimeField()
    notes=models.TextField(max_length=500,)
    status=models.ForeignKey('Status')
    
    class Meta:
        verbose_name_plural = 'Processes'
        
class Flow(FlowBluePrint, models.Model):
    pass
    
    
class Comment(models.Model):
    comment=models.TextField(max_length=1000,)
    date_submitted=models.DateTimeField()
    user_submitted=models.ForeignKey('auth.User')
    
    def submit(self):
        self.date_submitted = timezone.now()
        self.save()
    
    def __str__(self):
        return '\n '.join(self.date_submitted,
                        self.user_submitted,
                        self.comment)

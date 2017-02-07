from django.contrib import admin
from .models import Project, ProcessBluePrint,Process,ActivityBluePrint,Activity,Action,FlowBluePrint,Flow,\
ProcessType,ProdLine,Business,Comment, Status
 
admin.site.register(Project)
admin.site.register(ProcessBluePrint)
admin.site.register(Process)
admin.site.register(ActivityBluePrint)
admin.site.register(Activity)
admin.site.register(Action)
admin.site.register(FlowBluePrint)
admin.site.register(Flow)
admin.site.register(ProcessType)
admin.site.register(ProdLine)
admin.site.register(Business)
admin.site.register(Comment)
admin.site.register(Status)

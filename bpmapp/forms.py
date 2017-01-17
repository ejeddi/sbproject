from django import forms
from .models import Project, ProcessBluePrint,Process,ActivityBluePrint,Activity,Action,FlowBluePrint,Flow,\
ProcessType,ProdLine,Business,Comment, Status

class NewProcess(froms.ModelForm):

    class Meta:
        model=Process



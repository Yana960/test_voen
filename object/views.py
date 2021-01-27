from django.shortcuts import render
from .models import VeloObject
# Create your views here.
def showobject(request):
	object_marsh = VeloObject.objects
	return render(request, 'object/objects.html',  {'object_marsh': object_marsh})

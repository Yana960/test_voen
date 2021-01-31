from django.shortcuts import render
from .models import VeloMarsh,Quetion
# Create your views here.
def showmain(request):
	marhs = VeloMarsh.objects
	quetion = Quetion.objects
	return render(request, 'velo/main.html', {'marhs': marhs, 'quetion': quetion})

def articles(request):
	return render(request, 'velo/articles.html')

def about(request):
	return render(request, 'velo/about.html')

def objects(request):
	return render(request, 'velo/objects.html')

def navigator(request):
	return render(request, 'velo/navigator.html')

def saved(request):
	return render(request, 'velo/saved.html')

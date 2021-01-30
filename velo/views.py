from django.shortcuts import render
from .models import VeloMarsh

# Create your views here.
def showmain(request):
	marhs = VeloMarsh.objects
	return render(request, 'velo/main.html',  {'marhs': marhs})

def about(request):
	return render(request, 'velo/about.html')


def navigator(request):
	return render(request, 'velo/navigator.html')

def saved(request):
	return render(request, 'velo/saved.html')

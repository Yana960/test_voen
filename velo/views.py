from django.shortcuts import render

# Create your views here.
def showmain(request):
	return render(request, 'velo/main.html')
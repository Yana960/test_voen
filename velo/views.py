from django.shortcuts import render

# Create your views here.
def showmain(request):
	return render(request, 'velo/main.html')

def articles(request):
	return render(request, 'velo/articles.html')

def about(request):
	return render(request, 'velo/about.html')

def objects(request):
	return render(request, 'velo/objects.html')

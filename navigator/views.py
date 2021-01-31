from django.shortcuts import render

def navigator(request):
	return render(request, 'navigator/navigator.html')
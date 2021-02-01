from django.contrib.auth import authenticate
from django.shortcuts import render

# Create your views here.
def log_in(request):
    if ('username' in request.REQUEST) and ('password' in request.REQUEST):
        username = request.REQUEST['username']
        password = request.REQUEST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
    return render(request, 'login/login.html')
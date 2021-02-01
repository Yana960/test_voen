from django.shortcuts import render
from .models import VeloMarsh, HistoryMarsh


# Create your views here.
def showmain(request):
    marhs = VeloMarsh.objects
    return render(request, 'velo/main.html', {'marhs': marhs})


def about(request):
    return render(request, 'velo/about.html')


def navigator(request):
    return render(request, 'velo/navigator.html')


def saved(request):
    return render(request, 'velo/saved.html')


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def showohistorymarsh(request, marsh_id):
    history_marsh = HistoryMarsh.objects.all()
    marsh = VeloMarsh.objects.get(id=marsh_id)
    paginator = Paginator(history_marsh, 5)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        history_marsh = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        history_marsh = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        history_marsh = paginator.page(paginator.num_pages)
    return render(request, 'velo/route.html', {'history_marsh': history_marsh, 'marsh':marsh})

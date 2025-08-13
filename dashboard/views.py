from django.shortcuts import render

def home(request):
    return render(request, 'dashboard/index.html')
def index(request):

    data = {
        'title': "Landing Page' Dashboard",
    }

    return render(request, 'dashboard/index.html', data)
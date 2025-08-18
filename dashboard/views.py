from django.shortcuts import render, redirect
import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    # Verifica si el usuario está autenticado
    if not request.user.is_authenticated:
        # Redirige al login del admin y vuelve al dashboard tras iniciar sesión
        return redirect('/admin/login/?next=/')

    # Si está autenticado, carga los datos normalmente
    response = requests.get(settings.API_URL)
    posts = response.json()
    total_responses = len(posts)

    data = {
        'title': "Landing Page' Dashboard",
        'total_responses': total_responses,
    }

    return render(request, 'dashboard/index.html', data)

from django.contrib import admin
from django.urls import path
from dashboard.views import index  # Tu vista principal del dashboard
from django.contrib.auth import views as auth_views  # Importa las vistas de autenticación

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Dashboard principal
    path('', index, name='dashboard'),

    # Login
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='security/login.html'),
        name='login'
    ),

    # Logout
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='/login/'),
        name='logout'
    ),
]

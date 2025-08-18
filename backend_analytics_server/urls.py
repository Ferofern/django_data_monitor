from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from dashboard.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='dashboard'),

    # Login con plantilla dentro de dashboard/security
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='dashboard/security/login.html'),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='/login/'),
        name='logout'
    ),
]


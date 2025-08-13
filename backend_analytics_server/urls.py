from django.contrib import admin
from django.urls import path
from dashboard.views import home  # Importa la vista correcta

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='dashboard'),  # URL principal
]

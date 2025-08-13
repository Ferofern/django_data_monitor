from django.contrib import admin
from django.urls import path
from dashboard.views import index  # Importa la vista correcta

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='dashboard'),  # URL principal
]

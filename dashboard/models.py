from django.db import models

# Create your models here.

class DashboardPermission(models.Model):
    # Campo dummy requerido (no se usará)
    name = models.CharField(max_length=50, default="dashboard_permission")

    class Meta:
        permissions = [
            ("index_viewer", "Can show to index view (function-based)"),
        ]
        managed = False  # No crear tabla en la base de datos
        default_permissions = ()  # No crear permisos por defecto (add, change, delete, view)
        
    def __str__(self):
        return "Dashboard Permissions"
"""
URL configuration for academic_project project.
"""
from django.contrib import admin
from django.urls import path, include
from academic import views

# --- ENRUTADOR PRINCIPAL DEL PROYECTO ---
# Aquí se define el punto de entrada para todas las URLs del sitio.
urlpatterns = [
    # Solución al Requerimiento de Ruta Vacía ('/')
    # Cuando un usuario entra a la raíz del sitio, se llama a la vista home_view 
    # que renderiza directamente la plantilla de cursos, evitando el clásico error 404.
    path('', views.home_view, name='home'),
    
    # Ruta hacia el panel de administración por defecto de Django
    path('admin/', admin.site.urls),
    
    # Inclusión de las sub-rutas de la aplicación 'academic'
    # Al estar con el prefijo vacío (''), significa que las rutas como 'api/' o 'cursos/' 
    # se leerán directamente desde el dominio raíz (ej: localhost:8000/api/)
    path('', include('academic.urls')),
]

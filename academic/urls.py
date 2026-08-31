from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TeacherViewSet, CourseViewSet, StudentViewSet, StudentCourseViewSet,
    CoursesPageView, StudentsPageView, TeachersPageView
)

# --- ENRUTADOR DE LA API (DRF Router) ---
# El DefaultRouter crea automáticamente todas las rutas (URLs) CRUD necesarias para los ViewSets.
# Genera rutas como GET /api/teachers/, POST /api/teachers/, PUT /api/teachers/{id}/, etc.
# Esto conecta directamente cada ruta /api/... con su ViewSet respectivo.
router = DefaultRouter()
router.register(r'teachers', TeacherViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'students', StudentViewSet)
router.register(r'student-courses', StudentCourseViewSet)

urlpatterns = [
    # 1. Incluimos todas las rutas automáticas generadas por el Router bajo el prefijo 'api/'
    # Estas son las URLs que nuestro frontend (fetch) consumirá en JavaScript.
    path('api/', include(router.urls)),
    
    # 2. Rutas tradicionales para mostrar las páginas HTML en el navegador.
    # Conecta la ruta en el navegador (ej: localhost:8000/cursos/) con la Vista que retorna el HTML.
    path('cursos/', CoursesPageView.as_view(), name='courses_view'),
    path('estudiantes/', StudentsPageView.as_view(), name='students_view'),
    path('profesores/', TeachersPageView.as_view(), name='teachers_view'),
]

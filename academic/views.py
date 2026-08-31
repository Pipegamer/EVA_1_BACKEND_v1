from rest_framework import viewsets
from .models import Teacher, Course, Student, StudentCourse
from .serializers import TeacherSerializer, CourseSerializer, StudentSerializer, StudentCourseSerializer

from django.views.generic import TemplateView

# --- VISTAS DE LA API (BACKEND) ---
# Los ViewSets manejan automáticamente las acciones HTTP (GET, POST, PUT, PATCH, DELETE)
# para un modelo específico. 
# Conectan la información de la base de datos (Model.objects.all()) 
# y la pasan a través del Serializador (Serializer) para enviarla como JSON.

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all() # Trae todos los profesores
    serializer_class = TeacherSerializer # Utiliza este serializador para formarlos a JSON

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCourseViewSet(viewsets.ModelViewSet):
    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer

# --- VISTAS DE RENDERIZADO HTML (FRONTEND) ---
# Estas vistas se encargan de devolver archivos HTML al usuario (vistas tradicionales)
# En estos HTML es donde el frontend (JavaScript/fetch) hace las llamadas a las APIs de arriba.

class CoursesPageView(TemplateView):
    # Conecta la ruta con el archivo HTML de cursos
    template_name = 'academic/courses.html'

class StudentsPageView(TemplateView):
    # Conecta la ruta con el archivo HTML de estudiantes
    template_name = 'academic/students.html'

class TeachersPageView(TemplateView):
    # Conecta la ruta con el archivo HTML de profesores
    template_name = 'academic/teachers.html'

from django.shortcuts import render

# Vista básica (basada en función) que redirige la ruta raíz '/' 
# renderizando por defecto la vista de cursos.
def home_view(request):
    return render(request, 'academic/courses.html')

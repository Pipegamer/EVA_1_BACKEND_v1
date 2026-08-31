from rest_framework import serializers
from .models import Teacher, Course, Student, StudentCourse

# Los Serializers (Serializadores) son los encargados de transformar 
# los objetos complejos de Python (Modelos) en formatos fáciles de renderizar 
# como JSON para la API, y viceversa (de JSON a objetos de base de datos).
# Conectan directamente los Modelos con los ViewSets (Vistas de API).

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher # Indica el modelo base
        fields = '__all__' # Serializa todos los campos de la tabla

class CourseSerializer(serializers.ModelSerializer):
    # Campo extra de solo lectura para devolver el nombre completo del profesor (first_name + last_name)
    teacher_name = serializers.CharField(source='teacher.__str__', read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class StudentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourse
        fields = '__all__'

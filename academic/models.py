from django.db import models

# Modelo Teacher (Profesor)
# Representa la tabla de profesores en la base de datos.
# Está conectado con el modelo Course mediante una relación de uno a muchos.
class Teacher(models.Model):
    first_name = models.CharField(max_length=100) # Nombre del profesor
    last_name = models.CharField(max_length=100)  # Apellido del profesor

    def __str__(self):
        # Devuelve una representación en texto del objeto, útil en el admin de Django
        return f"{self.first_name} {self.last_name}"

# Modelo Course (Curso)
# Representa los cursos disponibles.
# Tiene una relación ForeignKey (Muchos a Uno) con Teacher: Un curso tiene un solo profesor,
# pero un profesor puede dictar muchos cursos.
class Course(models.Model):
    name = models.CharField(max_length=200)
    # on_delete=models.CASCADE indica que si se borra el profesor, también se borran sus cursos.
    # related_name='courses' permite acceder a los cursos de un profesor usando profesor.courses.all()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.name

# Modelo Student (Estudiante)
# Representa la tabla de estudiantes en la base de datos.
# Se relaciona con los cursos a través del modelo intermedio StudentCourse.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Modelo StudentCourse (Estudiante-Curso)
# Es una tabla intermedia que gestiona la relación Muchos a Muchos entre Student y Course.
# Es decir, un estudiante puede tener muchos cursos, y un curso muchos estudiantes.
class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        # unique_together evita que un mismo estudiante sea registrado dos veces en el mismo curso
        unique_together = ('student', 'course')
        verbose_name_plural = "Student Courses" # Nombre legible en el panel de administrador

    def __str__(self):
        return f"{self.student} - {self.course}"

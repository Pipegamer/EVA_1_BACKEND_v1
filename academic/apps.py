from django.apps import AppConfig

# Configuración principal de la aplicación 'academic'
# Este bloque le dice a Django cómo registrar e inicializar esta app dentro del proyecto global.
class AcademicConfig(AppConfig):
    name = 'academic' # Nombre de la aplicación (debe coincidir con la carpeta de la app)

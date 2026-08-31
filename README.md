# Sistema de Gestión Académica - Evaluación 1 (Backend)

Este proyecto corresponde a la **Evaluación N°1 de Desarrollo Backend con Django & DRF**. Es una plataforma que simula la gestión académica de estudiantes, cursos y profesores utilizando **Django**, **Django REST Framework (DRF)** y el consumo asíncrono desde el frontend mediante **Vanilla JavaScript (Fetch)** y **Bootstrap**.

## 📌 Requerimientos

1. **Modelo Entidad-Relación**: Tablas creadas correctamente (`Teacher`, `Course`, `Student`, `StudentCourse`).
2. **Simulación de Datos**: Incluye archivo `datos_prueba.json` o se puede usar el panel de administrador.
3. **Serializadores y Endpoints DRF**: API expuesta en `/api/` usando `ModelViewSet` y `DefaultRouter`.
4. **Vistas Tradicionales e Interfaz Web (HTML)**: Endpoints REST enmascarados con vistas HTML consumiendo JSON por debajo con peticiones Fetch (`GET`, `POST`, `PUT`, `DELETE`).
5. **Solución a Ruta Vacía**: La ruta raíz `/` renderiza el listado sin errores 404.
6. **Código Full Comentado**: Cada archivo clave (Modelos, Vistas, Rutas, Plantillas y JS) cuenta con explicaciones técnicas.
7. **Documentación IA**: Los prompts utilizados están registrados en el archivo `prompts.md`.

## 🚀 Instrucciones para Levantar el Proyecto

### 1. Activar el Entorno Virtual
Asegúrate de estar en la carpeta raíz del proyecto (donde se encuentra `manage.py`) y activa el entorno:
```bash
# En Windows (CMD o PowerShell)
.\env\Scripts\activate
```

### 2. Ejecutar las Migraciones (Opcional, si no están aplicadas)
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Levantar el Servidor de Desarrollo
```bash
python manage.py runserver
```

Una vez levantado, ingresa en tu navegador a: [http://localhost:8000/](http://localhost:8000/)

---

## 🔑 Credenciales de Acceso (Panel de Administración)

Para gestionar los registros desde el backend de forma nativa, visita [http://localhost:8000/admin/](http://localhost:8000/admin/) e ingresa con las siguientes credenciales:

- **Usuario:** `profe`
- **Contraseña:** *profe123*

---
*Desarrollado para la asignatura de Desarrollo Backend.*

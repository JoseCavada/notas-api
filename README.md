# Notas API
Esta es una API para gestionar notas con autenticación JWT en Django REST Framework.

## 🚀Funcionalidades
- Registro de usuarios

- Autenticación con JWT

- CRUD de notas

- Protección de endpoints con autenticación

## 📖Endpoints
### 🔐Autenticación y Usuarios
| Método | Endpoint      | Descripción             |
|:-------|:--------------| :----------             |
|POST    |/registro/     |Registra un nuevo usuario|
|POST    |/token/        |Obtiene token JWT de acceso y refresco
|POST    |/token/refresh/|Renueva un token de acceso usando el refresh token                                      |  


Ejemplo de JSON para registrar un usuario:
```
{ "username": "usuario123",
  "email": "usuario@email.com",
  "password": "contraseña_segura" }
```
Ejemplo de JSON para obtener un token:
```
{ "username": "usuario123",
  "password": "contraseña_segura" }
```
Respuesta esperada:
```
{ "access": "token_de_acceso",
  "refresh": "token_de_refresco" }
```
### 📝Gestión de Notas
| Método | Endpoint      | Descripción             |
|:-------|:--------------| :----------             |
|POST|/notas/|Crea una nueva nota (requiere autenticación)
|GET|/notas/| Obtiene todas las notas del usuario autenticado
|GET|/notas/{id}/| Obtiene una nota específica
|PUT|/notas/{id}/|Actualiza una nota existente
|DELETE|/notas/{id}/|Elimina una nota existente


Ejemplo de JSON para crear una nota:
```
{ "titulo": "Mi primera nota", "contenido": "Este es un contenido de prueba" }
```
Para autenticarse, incluir el token en los headers:
```
Authorization: Bearer <token_de_acceso>
```

## 📑Documentación Swagger
La API incluye documentación Swagger UI, accesible en:
http://localhost:8000/swagger/

Para visualizarla, iniciar el servidor y acceder a la URL en el navegador.

## 🛠Tecnologías Utilizadas
Django

Django REST Framework

drf-yasg (Swagger)

djangorestframework-simplejwt (JWT)

Microsoft SQL Server

## 📦Instalación y Configuración
1. Clonar el repositorio
```

git clone [URL del repositorio en GitHub]
cd [nombre del repositorio]
```
2. Crear entorno virtual e instalar dependencias
```
python -m venv venv
source venv/bin/activate (En Windows usa venv\Scripts\activate)
pip install -r requirements.txt
```
3. Aplicar migraciones
```
python manage.py migrate
```

4. Crear un superusuario (opcional, para administración)
```
python manage.py createsuperuser
```

5. Iniciar el servidor
```
python manage.py runserver
```

## 📜Archivo requirements.txt
```
Django= 5.0.13

djangorestframework= 3.15.2

djangorestframework-simplejwt= 5.5.0

drf-yasg= 1.21.10

mssql-django= 1.5
```

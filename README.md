# Django Test Project

Este proyecto de Django implementa un modelo básico, vistas, y pruebas automatizadas para demostrar el uso de las capacidades de prueba integradas de Django. Además, incluye un script para cargar información en la base de datos.

## Características

1. **Modelo Item:** Representa un elemento con los campos:
   - Nombre
   - Descripción
   - Precio

2. **Pruebas Automatizadas:**
   - Pruebas de modelos.
   - Pruebas de vistas.

3. **Script de carga:** Un script independiente para cargar datos en la base de datos usando el módulo `os`.

4. **Interfaz de Usuario:** Una vista sencilla para listar los elementos almacenados en la base de datos.

## Requisitos Previos

- Python 3.8+
- Django 5.1.5

## Instalación

1. Clona este repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   ```

2. Ve al directorio del proyecto:
   ```bash
   cd test_project
   ```

3. Crea un entorno virtual:
   ```bash
   python -m venv venv
   ```

4. Activa el entorno virtual:
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

6. Realiza las migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Crea un superusuario:
   ```bash
   python manage.py createsuperuser
   ```

8. Inicia el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

9. Accede a la aplicación en tu navegador:
   - Panel de Administración: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
   - Página de Inicio: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Uso del Script de Carga

1. Asegúrate de que el entorno virtual esté activado.

2. Ejecuta el script para cargar datos en la base de datos:
   ```bash
   python load_data.py
   ```

3. Verifica los datos cargados en la página de inicio o en el panel de administración.

## Estructura del Proyecto

```
test_project/
├── manage.py
├── test_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── app_tests/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   ├── __init__.py
│   ├── models.py
│   ├── templates/
│   │   ├── item_list.html
│   ├── tests.py
│   ├── views.py
├── load_data.py
```

## Pruebas Automatizadas

Ejecuta las pruebas con el siguiente comando:
```bash
python manage.py test
```

El proyecto incluye:
- Pruebas de creación y consulta de elementos en la base de datos.
- Pruebas de la vista principal para verificar que la lista de elementos se carga correctamente.

## Licencia
Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.

## Contribuciones
Si deseas contribuir, envía un pull request o abre un issue con tus sugerencias.

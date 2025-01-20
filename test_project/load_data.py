import os
import django

# Configurar las variables de entorno para acceder a la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_project.settings')
django.setup()

from app_tests.models import Item

# Datos a cargar
data = [
    {"name": "Item 1", "description": "Description for Item 1", "price": 10.50},
    {"name": "Item 2", "description": "Description for Item 2", "price": 20.75},
    {"name": "Item 3", "description": "Description for Item 3", "price": 15.00},
    {"name": "Item 4", "description": "Description for Item 4", "price": 30.25},
]

# Función para cargar los datos
def load_items():
    for entry in data:
        item, created = Item.objects.get_or_create(
            name=entry["name"],
            defaults={
                "description": entry["description"],
                "price": entry["price"],
            },
        )
        if created:
            print(f"Creado: {item}")
        else:
            print(f"Ya existía: {item}")

if __name__ == '__main__':
    load_items()

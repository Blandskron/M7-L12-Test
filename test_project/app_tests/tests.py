from django.test import TestCase, Client
from .models import Item

class ItemModelTest(TestCase):
    def setUp(self):
        Item.objects.create(name="Item 1", description="Description 1", price=10.0)
        Item.objects.create(name="Item 2", description="Description 2", price=20.0)

    def test_item_creation(self):
        item = Item.objects.get(name="Item 1")
        self.assertEqual(item.description, "Description 1")
        self.assertEqual(item.price, 10.0)

class ItemViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        Item.objects.create(name="Item 1", description="Description 1", price=10.0)

    def test_item_list_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Item 1")

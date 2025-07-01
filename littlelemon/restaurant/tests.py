from django.test import TestCase

# Create your tests here.

from restaurant.models import Menu,Booking
from decimal import Decimal

class MenuTest(TestCase):
    def test_get_item(self):
        # Create a test instance of the Menu model
        item = Menu.objects.create(title="IceCream", price=5.99, inventory=100)

class MenuTest(TestCase):
    def test_get_item(self):
        # Create a test instance of the Menu model
        item = Menu.objects.create(
            title="IceCream",
            price=Decimal('80.00'),
            inventory=100
        )
        
        # Call the __str__ method by casting the object to a string
        item_str = str(item)
        
        # Create the expected string representation
        expected_string = "IceCream : 80.00"
        
        # Use assertEqual to compare the string representation of the object
        # to the expected string. str(item) will call the __str__ method.
        self.assertEqual(str(item), expected_string)
#testing views

from django.test import TestCase, Client
from django.urls import reverse
from rshop.views import home,cart

class TestViews(TestCase):
     
     def setUp(self):
          self.client = Client()
          self.urls_home = reverse('home')
          self.urls_cart = reverse('cart')

     
     def test_views_home(self):
          response = self.client.get(self.urls_home)
          self.assertEqual(response.status_code,200)
          self.assertTemplateUsed(response,'home.html')

     def test_views_cart(self):
          response = self.client.get(self.urls_cart)
          self.assertEqual(response.status_code,200)
          self.assertTemplateUsed(response,'cart.html')
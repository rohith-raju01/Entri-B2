#testing Urls

from django.test import SimpleTestCase
from django.urls import reverse,resolve
from rshop.views import home


class TestUrls(SimpleTestCase):
    def test_home(self):
        urls = reverse('home')
        print(resolve(urls))
        self.assertEquals(resolve(urls).func, home)

#testing Urls with slug

from django.test import SimpleTestCase
from django.urls import resolve, reverse
from shop.views import allproducts
class TestURL(SimpleTestCase):
    def testurlhome(self):
        url=reverse('product_by_category', args=['demo-slug'])
        self.assertEquals(resolve(url).func, allproducts)
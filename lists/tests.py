from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page

class HomePage(TestCase):

    def test_url_resovles_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


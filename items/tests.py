from django.test import TestCase
from django.urls import reverse

from .models import Item


class ItemTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.item = Item.objects.create(text="Tea")

    def test_model_conent(self):
        self.assertEqual(self.item.text, "Tea")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Tea")

from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Note, Category

User = get_user_model()


class BaseTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(email="test@example.com", password="12345", username="test")
        cls.wrong_user = User.objects.create_user(email="wrong@example.com", password="12345", username="wrong")
        cls.note = Note.objects.create(title="test", description="test", user=cls.user)
        cls.category = Category.objects.create(title="test", color="#FFFFFF", user=cls.user)

class TestViews(BaseTest):
    def redirect_if_not_logged_in(self, url):
        response = self.client.get(url)
        self.assertRedirects(response, '/login/?next='+ url)

    def redirect_if_logged_in(self, url):
        self.client.force_login(self.user)  
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def access_to_own_instance(self, url):
        self.client.force_login(self.user)  
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def access_to_not_your_instance(self, url):
        self.client.force_login(self.wrong_user)  
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)
        
class NoteListViewTest(TestViews):
    def test_note_list_view(self):
        self.redirect_if_not_logged_in("/notes/")
        self.redirect_if_logged_in("/notes/")


class NoteUpdateViewTest(TestViews):
    def test_note_update_view(self):
        self.access_to_own_instance(f"/notes/{self.note.pk}/update")
        self.access_to_not_your_instance(f"/notes/{self.note.pk}/update")


class NoteDeleteViewTest(TestViews):
    def test_note_delete_view(self):
        self.access_to_own_instance(f"/notes/{self.note.pk}/delete")
        self.access_to_not_your_instance(f"/notes/{self.note.pk}/delete")
    
    
class NoteChangeStatus(TestViews):
    def test_category_update_view(self):
        # self.access_to_own_instance(f"/notes/{self.note.pk}/note_status")
        self.access_to_not_your_instance(f"/notes/{self.note.pk}/note_status")

class CategoryListViewTest(TestViews):
    def test_category_list_view(self):
        self.redirect_if_not_logged_in("/categories/")
        self.redirect_if_logged_in("/categories/")

class CategoryUpdateViewTest(TestViews):
    def test_category_update_view(self):
        self.access_to_own_instance(f"/category/{self.category.pk}/update")
        self.access_to_not_your_instance(f"/category/{self.category.pk}/update")

class CategoryDeleteViewTest(TestViews):
    def test_category_delete_view(self):
        self.access_to_own_instance(f"/category/{self.category.pk}/delete")
        self.access_to_not_your_instance(f"/category/{self.category.pk}/delete")



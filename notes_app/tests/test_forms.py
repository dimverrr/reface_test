from django.test import TestCase
from ..forms import NoteForm, CategoryForm, CustomUserForm
from django.contrib.auth.models import User


class TestCategoryForm(TestCase):
    def test_category_form_fields(self):
        form = CategoryForm()
        self.assertEqual(set(form.fields.keys()), {'title', 'color'})

class TestNoteForm(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

    def test_note_form_fields(self):
        form = NoteForm(user=self.user)
        self.assertEqual(set(form.fields.keys()), {'title', 'description', 'category'})


class TestCustomUserForm(TestCase):
    def test_custom_user_form_fields(self):
        form = CustomUserForm()
        self.assertEqual(set(form.fields.keys()), {'username', 'email', 'password1', 'password2'})
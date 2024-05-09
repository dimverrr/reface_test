from django.test import TestCase
from ..models import Note, Category
from django.contrib.auth import get_user_model
from ..models import Note, Category

User = get_user_model()

class BaseTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(email="test@example.com", password="12345", username="test_user")
        cls.note = Note.objects.create(title="test", description="test Test one", user=cls.user)
        cls.category = Category.objects.create(title="test", color="#FFFFFF", user=cls.user)

    def field_max_length(self, field_name, max_len):
        max_length = self.note._meta.get_field(field_name).max_length
        self.assertEqual(max_length, max_len)
    
class NoteModelTest(BaseTest):
    def test_total_words_count(self):
        self.assertEqual(self.note.words_count, 3)
    
    def test_unique_words_count(self):
        self.assertEqual(self.note.unique_words_count, 2)

    def test_title_max_length(self):
        self.field_max_length("title", 20)

    def test_description_max_length(self):
        self.field_max_length("description", 200)


class CategoryModelTest(BaseTest):
    def test_title_max_length(self):
        self.field_max_length("title", 20)



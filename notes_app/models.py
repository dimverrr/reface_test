from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    words_count = models.IntegerField(editable=False)
    unique_words_count = models.IntegerField(editable=False)
    is_archived = models.BooleanField(default=False)
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.words_count = self.count_total_words()
        self.unique_words_count = self.count_unique_words()
        super(Note, self).save(*args, **kwargs)

    def count_total_words(self):
        total_words = self.description.lower().split()
        return len(total_words)
    
    def count_unique_words(self):
        total_unique_words = set(self.description.lower().split())
        return len(total_unique_words)
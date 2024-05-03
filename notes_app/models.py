from django.db import models
from colorfield.fields import ColorField
# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    color = ColorField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    words_count = models.IntegerField(editable=False)
    unique_words_count = models.IntegerField(editable=False)
    is_archived = models.BooleanField(default=False)
    category= models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["is_archived"]
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        words_count = self.count_total_words()
        unique_words_count = set(self.count_total_words())
        
        self.words_count = len(words_count)
        self.unique_words_count = len(unique_words_count)
        
        super(Note, self).save(*args, **kwargs)

    def count_total_words(self):
        total_words = self.description.lower().split()
        return total_words
    
    # def count_unique_words(self):
    #     total_unique_words = set(self.description.lower().split())
    #     return len(total_unique_words)
from django import forms
from .models import Category, Note
from colorfield.widgets import ColorWidget
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', "color"]
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}), "color":ColorWidget()}

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'description', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',}),
            'description': forms.Textarea(attrs={'class': 'form-control',}),
        }
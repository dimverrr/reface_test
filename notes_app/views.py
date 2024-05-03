from django.views.generic  import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Category, Note
from .forms import CategoryForm, NoteForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

# Create your views here.

class NoteListView(ListView):
    model = Note
    context_object_name = 'note_list'
    template_name = "note_list.html"

    def get_queryset(self):
        queryset = Note.objects.all()
        filters = ["-words_count", "-unique_words_count", "-category", "-is_archived", "is_archived"]

        query_parameter = self.request.GET.get('filter_by')
        if  query_parameter in filters:
            queryset = queryset.order_by(str(query_parameter))

        return queryset
    
class NoteDetailView(DetailView):
    model = Note 
    template_name="note_detail.html"

class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name= "note_form.html"
    success_url=reverse_lazy("note_list")

class NoteUpdateView(UpdateView):
    model = Note 
    form_class = NoteForm
    template_name= "note_form.html"
    success_url=reverse_lazy("note_list")

class NoteDeleteView(DeleteView):
    model = Note
    template_name= "note_delete.html"
    success_url=reverse_lazy("note_list")

    
def change_archive_status(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.is_archived = not note.is_archived
    note.save()
    return redirect("/notes")
    
class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories_list'

    def get_queryset(self):
        return Category.objects.order_by("name")
    
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name='category_form.html'
    success_url=reverse_lazy("note_list")
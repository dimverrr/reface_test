from django.views.generic  import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Category, Note
from .forms import CategoryForm, NoteForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return render(request, 'index.html')

# !!!!!!
# Перенести логику в модель?
class NoteListView(ListView):
    model = Note
    context_object_name = 'note_list'
    template_name = "note_list.html"

    def get_queryset(self):
        queryset = Note.objects.all()

        filter_by_word_count = self.request.GET.get('filter_by_word_count')
        if  filter_by_word_count:
            queryset = queryset.order_by("-words_count")

        filter_by_unique_word_count = self.request.GET.get('filter_by_unique_word_count')
        if filter_by_unique_word_count:
            queryset = queryset.order_by("-unique_words_count")

        filter_by_category = self.request.GET.get('filter_by_category')
        if filter_by_category:
            queryset = queryset.order_by("-category")
        
        filter_by_archived = self.request.GET.get("filter_by_archived")
        if filter_by_archived:
            queryset = queryset.order_by("-is_archived")

        filter_by_active = self.request.GET.get("filter_by_active")
        if filter_by_active:
            queryset = queryset.order_by("is_archived")

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

# class NoteDeleteView(DeleteView):
#     model = Note
#     template_name= "note_delete.html"
#     success_url=reverse_lazy("note_list")

def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    note.delete()
    return HttpResponse()

    
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
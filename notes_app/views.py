from django.views.generic  import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Category, Note
from .forms import CategoryForm, NoteForm, CustomUserForm
from .mixins import PermissionMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy

from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView


# Create your views here.
class UserSignup(FormView):
	template_name = 'signup.html'
	form_class = CustomUserForm
	redirect_authenticated_user = True
	success_url = reverse_lazy('note_list')
    
	def form_valid(self, form):
		user = form.save()
		if user is not None:
			login(self.request, user)
		return super(UserSignup, self).form_valid(form)

	def get(self, *args, **kwargs):
		if self.request.user.is_authenticated:
			return redirect('note_list')
		return super(UserSignup, self).get(*args, **kwargs)
     
class UserLogin(LoginView):
	template_name = 'login.html'
	fields = '__all__'
	redirect_authenticated_user = True

	def get_success_url(self):
		return reverse_lazy('note_list')



class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = 'note_list'
    template_name = "note_list.html"

    def get_queryset(self):
        queryset = Note.objects.filter(user=self.request.user)
        filters = ["-words_count", "-unique_words_count", "-category", "-is_archived", "is_archived"]

        query_parameter = self.request.GET.get('filter_by')
        if  query_parameter in filters:
            queryset = queryset.order_by(str(query_parameter))

        return queryset
    
# class NoteDetailView(LoginRequiredMixin, PermissionMixin, DetailView):
#     model = Note 
#     template_name="note_detail.html"

class NoteCreateView(LoginRequiredMixin,CreateView):
    model = Note
    form_class = NoteForm
    template_name= "note_form.html"
    success_url=reverse_lazy("note_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class NoteUpdateView(LoginRequiredMixin, PermissionMixin, UpdateView):
    model = Note 
    form_class = NoteForm
    template_name= "note_form.html"
    success_url=reverse_lazy("note_list")

    
class NoteDeleteView(LoginRequiredMixin, PermissionMixin, DeleteView):
    model = Note
    template_name= "note_delete.html"
    success_url=reverse_lazy("note_list")

    
def change_archive_status(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.is_archived = not note.is_archived
    note.save()
    return redirect("/notes")
    
class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories_list'
    
    def get_queryset(self):
        queryset = Category.objects.filter(user=self.request.user)
        return queryset
    
class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name='category_form.html'
    success_url=reverse_lazy("categories_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class CategoryUpdateView(LoginRequiredMixin, PermissionMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name='category_form.html'
    success_url=reverse_lazy("categories_list")

class CategoryDeleteView(LoginRequiredMixin, PermissionMixin, DeleteView):
    model = Category
    template_name= "category_delete.html"
    success_url=reverse_lazy("categories_list")
from django.urls import path
from .views import index, NoteListView, NoteDetailView, NoteCreateView, NoteUpdateView, change_archive_status, CategoryCreateView, delete_note, CategoryListView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='categories_list'),
    path('categories/create/', CategoryCreateView.as_view(), name="category_create"),
    path("notes/", NoteListView.as_view(), name="note_list"),
    path("notes/<int:pk>/", NoteDetailView.as_view(), name="note_detail"),
    path("notes/create/", NoteCreateView.as_view(), name= "note_create" ), 
    path("notes/<int:pk>/update", NoteUpdateView.as_view(), name="note_update"),
    # path("notes/<int:pk>/delete", NoteDeleteView.as_view(), name="note_delete"),
    path("notes/<int:pk>/delete", delete_note, name="note_delete"),
    path("notes/<int:pk>/note_status", change_archive_status, name="change_archive_status"),
    path('index/', index, name="index")
]
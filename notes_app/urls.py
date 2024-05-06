from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='login'),
    path('signup/', views.UserSignup.as_view(), name='signup'),
    path('logout/', views.logout_user, name='logout'),

    path('categories/', views.CategoryListView.as_view(), name='categories_list'),
    path('categories/create/', views.CategoryCreateView.as_view(), name="category_create"),
    path("category/<int:pk>/update", views.CategoryUpdateView.as_view(), name="category_update"),
    path("category/<int:pk>/delete", views.CategoryDeleteView.as_view(), name="category_delete"),

    path("notes/", views.NoteListView.as_view(), name="note_list"),
    path("notes/create/", views.NoteCreateView.as_view(), name= "note_create" ), 
    path("notes/<int:pk>/update", views.NoteUpdateView.as_view(), name="note_update"),
    path("notes/<int:pk>/delete", views.NoteDeleteView.as_view(), name="note_delete"),
    path("notes/<int:pk>/note_status", views.change_archive_status, name="change_archive_status"),
]
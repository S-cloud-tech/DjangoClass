from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('book/', views.show_book, name="books"),
    path('category/', views.show_categories, name="category"),

    path('add_book/', views.add_book, name="add_book"),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
]



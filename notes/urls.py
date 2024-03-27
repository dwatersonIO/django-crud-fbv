from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('update_note/<str:pk>/', views.update_note, name="update_note"),
    path('search_note/', views.search_note, name="search_note"),
	path('delete/<str:pk>/', views.delete_note, name="delete_note"),
]
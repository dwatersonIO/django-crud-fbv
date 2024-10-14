from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
    path('detail_note/<str:pk>', views.detail_note, name="detail_note"),
    path('create_note/', views.create_note, name="create_note"),
	path('update_note/<str:pk>/', views.update_note, name="update_note"),
    path('search_note/', views.search_note, name="search_note"),
	path('delete/<str:pk>/', views.delete_note, name="delete_note"),
    path('create_tag/', views.create_tag, name="create_tag"),
    path('h_search_note/', views.h_search_note, name="h_search_note"),
    path('h_search_note_tag/', views.h_search_note_tag, name="h_search_note_tag"),
]
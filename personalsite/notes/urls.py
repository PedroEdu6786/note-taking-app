from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('collection-list/', views.collection_list, name='collection-list'),
    path('collection-detail/<str:pk>/', views.collection_detail, name='collection-detail'),
    path('collection-create/', views.collection_create, name='collection-create'),
    path('collection-update/<str:pk>/', views.collection_update, name='collection-update'),
    path('collection-delete/<str:pk>/', views.collection_delete, name='collection-delete'),
    
    path('collection/<str:collection_id>/note-list/', views.note_list, name='note-list'),
    path('collection/note-detail/<str:pk>/', views.note_detail, name='note-detail'),
    path('collection/note-create/', views.note_create, name='note-create'),
    path('collection/note-update/<str:pk>/', views.note_update, name='note-update'),
    path('collection/note-delete/<str:pk>/', views.note_delete, name='note-delete'),
]
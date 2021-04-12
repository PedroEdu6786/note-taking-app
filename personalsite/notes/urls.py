from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('collection-list/', views.collection_list, name='collection-list'),
    path('collection-detail/<str:pk>/', views.collection_detail, name='collection-detail'),
    path('collection-create/', views.collection_create, name='collection-create'),
    path('collection-update/<str:pk>/', views.collection_update, name='collection-update'),
    path('collection-delete/<str:pk>/', views.collection_delete, name='collection-delete'),
]
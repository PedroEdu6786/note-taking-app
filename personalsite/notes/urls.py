from django.urls import path

from . import views

"""
/
    - show all collections, create new collection
    
/collection_id
    - show all notes of specified collection
    
/collection_id/note_id/
    - show note info
    
/collection_id/note/
    - lets you create new note
    
/collection/
    - lets you create new collection
"""

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:collection_id>/', views.collection, name='collection'),
    path('<int:collection_id>/<int:note_id>/', views.note, name='note'),
    path('<int:collection_id>/note/', views.create_note, name='newnote'),
    path('collection/', views.create_collection, name='newcollection'),
]
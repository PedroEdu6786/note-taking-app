from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Collection
from .serializers import CollectionSerializer, NoteSerializer

@api_view(['GET'])
def index(request):
    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>',
        'Create':'/task-create/',
    }
    
    return Response(api_urls)

@api_view(['GET'])
def collection_list(request):
    collections = Collection.objects.all()
    serializer = CollectionSerializer(collections, many=True)
    return Response(serializer.data)    

@api_view(['GET'])
def collection_detail(request, pk):
    collection = Collection.objects.get(id=pk)
    serializer = CollectionSerializer(collection, many=False)
    return Response(serializer.data)
    
@api_view(['POST'])
def collection_create(request):
    serializer = CollectionSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)
    
@api_view(['PUT'])
def collection_update(request, pk):
    collection = Collection.objects.get(id=pk)
    serializer = CollectionSerializer(instance=collection, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)
    
@api_view(['DELETE'])
def collection_delete(request, pk):
    collection = Collection.objects.get(id=pk)
    collection.delete()
    
    return Response('deleted')
    

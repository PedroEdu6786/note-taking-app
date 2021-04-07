# from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    
def note(request):
    return HttpResponse("Hello, world. You're at the polls note.")
    
def collection(request):
    return HttpResponse("Hello, world. You're at the polls collection.")
    
def create_note(request):
    return HttpResponse("Hello, world. You're at the polls create_note.")
    
def create_collection(request):
    return HttpResponse("Hello, world. You're at the polls create_collection.")
    
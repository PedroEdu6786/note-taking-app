from django.db import models

# Create your models here.
class Collection(models.Model):
    collection_name  = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
class Note(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    note_title = models.CharField(max_length=100)
    note_description = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')
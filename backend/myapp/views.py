# myapp/views.py

from rest_framework import viewsets
from .models import MyModel
from .serializers import MyModelSerializer
from django.http import HttpResponse
 

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

# myapp/views.py

from rest_framework import viewsets
from .models import MyModel
from .serializers import MyModelSerializer
from django.http import HttpResponse
 

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

def index(request):
    return HttpResponse("Welcome to the API root. Use /api/mymodel/ to access the data.")

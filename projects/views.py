from rest_framework import generics
from .serializers import *
from .models import *

# Create your views here.

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
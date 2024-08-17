from rest_framework import generics
from .serializers import *
from .models import *

# Create your views here.

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    def perform_create(self, serializer):
        try:
            serializer.save(owner=self.request.user)
        except:
            serializer.save()

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
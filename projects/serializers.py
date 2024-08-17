from rest_framework import serializers
from .models import *

class ProjectSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()
    notes = serializers.SerializerMethodField()
    texts = serializers.SerializerMethodField()

    def get_tasks(self, obj):
        tasks = Task.objects.filter(project=obj)
        return TaskSerializer(tasks, many=True).data
    
    def get_notes(self, obj):
        notes = Note.objects.filter(project=obj)
        return NoteSerializer(notes, many=True).data
    
    def get_texts(self, obj):
        texts = Text.objects.filter(project=obj)
        return TextSerializer(texts, many=True).data

    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['owner']

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = '__all__'

class TextSerializer(serializers.ModelSerializer):

    class Meta:
        model = Text
        fields = '__all__'
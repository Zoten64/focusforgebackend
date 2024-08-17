import uuid
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectList.as_view()),
    path('<uuid:pk>', views.ProjectDetail.as_view()),
]
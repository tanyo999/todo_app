from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *


class ListTodo(generics.ListAPIView):  # Read
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class DetailTodo(generics.RetrieveUpdateAPIView):  # update
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class CreateTodo(generics.CreateAPIView):  # create
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class DeleteTodo(generics.DestroyAPIView):  # Delete
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

# Create your views here.

# tasks/views.py
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

# View untuk mengambil semua tugas dan membuat tugas baru
class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# View untuk mengambil, memperbarui, dan menghapus tugas berdasarkan ID
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

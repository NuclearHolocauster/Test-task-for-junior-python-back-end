from rest_framework import generics
from .serializer import *
from .models import Student, Group


class StudentCreateView(generics.CreateAPIView):
    serializer_class = StudentSerializer


class GroupCreateView(generics.CreateAPIView):
    serializer_class = GroupSerializer


class StudentsListView(generics.ListAPIView):
    serializer_class = StudentsListSerializer
    queryset = Student.objects.all()


class GroupsListView(generics.ListAPIView):
    serializer_class = GroupsListSerializer
    queryset = Group.objects.all()


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

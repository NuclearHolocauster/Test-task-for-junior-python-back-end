from django.urls import path, include
from .views import *


app_name = 'main'
urlpatterns = [
    path('student/create/', StudentCreateView.as_view()),
    path('group/create/', GroupCreateView.as_view()),
    path('students', StudentsListView.as_view()),
    path('groups', GroupsListView.as_view()),
    path('student/<int:pk>', StudentDetailView.as_view()),
    path('group/<int:pk>', GroupDetailView.as_view())
]

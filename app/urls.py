from django.urls import path
from .views import *

urlpatterns = [
    path('home/', FanListView.as_view(), name='home'),
    path('fans/<int:pk>/', FanDetailView.as_view(), name='fan'),
    path('fans/create/', FanCreateView.as_view(), name='add_fan'),
    path('fans/<int:pk>/update/', FanUpdateView.as_view(), name='add_fan'),
    # path('fans/<int:pk>/delete/', FanDeleteView.as_view(), name='fan_delete'),
    path('students/', StudentListView.as_view(), name='home'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_about'),
    path('students/create/', StudentCreateView.as_view(), name='add_student'),
    path('students/<int:pk>/update/', StudentUpdateView.as_view(), name='add_student'),
    # path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
]

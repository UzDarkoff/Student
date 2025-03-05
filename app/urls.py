
from django.urls import path
from .views import *
urlpatterns = [
    path('home/', home,name='home'),
    path('fan/<int:fan_id>', fan,name='fan'),
    path('student_about/<int:student_id>', student_about,name='student_about'),
    path('add_student/', add_student,name='add_student'),
    path('add_fan/', add_fan,name='add_fan'),
]

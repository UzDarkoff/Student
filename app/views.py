from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Fan, Student
from .forms import FanForm, StudentForm


class FanListView(ListView):
    model = Fan
    template_name = 'home.html'
    context_object_name = 'home'


class FanDetailView(DetailView):
    model = Fan
    template_name = 'fan.html'
    context_object_name = 'fan'


class FanCreateView(CreateView):
    model = Fan
    form_class = FanForm
    template_name = 'add_fan.html'
    success_url = reverse_lazy('fan_list')


class FanUpdateView(UpdateView):
    model = Fan
    form_class = FanForm
    template_name = 'add_fan.html'
    success_url = reverse_lazy('fan_list')


# class FanDeleteView(DeleteView):
#     model = Fan
#     template_name = 'fan_confirm_delete.html'
#     success_url = reverse_lazy('fan_list')


class StudentListView(ListView):
    model = Student
    template_name = 'home.html'
    context_object_name = 'students'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_about.html'
    context_object_name = 'student'


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'add_student.html'
    success_url = reverse_lazy('student_list')


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'add_student.html'
    success_url = reverse_lazy('student_list')


# class StudentDeleteView(DeleteView):
#     model = Student
#     template_name = 'student_confirm_delete.html'
#     success_url = reverse_lazy('student_list')

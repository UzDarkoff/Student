from django import forms
from .models import Fan, Student


class FanForm(forms.ModelForm):
    class Meta:
        model = Fan
        fields = ['name']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'phone_number', 'email', 'address', 'fan']

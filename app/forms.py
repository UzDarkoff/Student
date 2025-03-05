
from .models import Fan, Student
from django import forms


class StudentForm(forms.Form):
    full_name = forms.CharField(max_length=150, label='Full_name',
                                widget=forms.TextInput(attrs={"class": "form-control"}))
    phone_number = forms.CharField(max_length=13, label='Phone', widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.CharField(max_length=100, label='Email', required=False, widget=forms.TextInput(attrs={"class": "form_control"}))
    address = forms.CharField(label='Address', max_length=150,widget=forms.TextInput(attrs={"class":"form-control"}))
    fan = forms.ModelChoiceField(empty_label='Choose fan', label='Fan',
                                      queryset=Fan.objects.all(),
                                      widget=forms.Select(attrs={"class": "form-control"}))


class FanForm(forms.Form):
    name = forms.CharField(max_length=50, label='Title', widget=forms.TextInput(attrs={"class": "form-control"}))

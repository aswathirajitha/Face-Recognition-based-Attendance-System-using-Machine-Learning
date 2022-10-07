from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from webapp.models import details,leave,disp

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','password1','password2']

class StudentForm(forms.ModelForm):
    class Meta:
        model=details
        fields='__all__'

class leaveForm(forms.ModelForm):
    class Meta:
        model=leave
        fields='__all__' 
        
    #     date = forms.DateTimeField(
    #     input_formats=['%d/%m/%Y %H:%M'],
    #     widget=forms.DateTimeInput(attrs={
    #         'class': 'form-control datetimepicker-input',
    #         'data-target': '#datetimepicker1'
        
    #     })
    # )
class displayForm(forms.ModelForm):
    class Meta:
        model=disp
        fields='__all__' 
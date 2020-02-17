from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,UserData



class UserForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = [
            'UFname', 
            'ULname', 
            'Upassword', 
            'Uemailid', 
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'username',
            'phone_number',
            'birth_date',
            
        ] 
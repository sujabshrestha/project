from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
class UserRegisterForm(UserCreationForm):
    # firstname = forms.CharField(max_length=30)
    # lastname = forms.CharField(max_length=30)
    email = forms.EmailField()



    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class userupdateform(forms.ModelForm):

    class Meta:
        model = User 
        fields = ['username','email']

class profileupdateform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


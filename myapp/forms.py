from django import forms
from myapp.models import*
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class contactform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=contact


class signupform(UserCreationForm):
        class Meta:
         fields=('first_name','last_name','username','email','password1','password2')
         model=User



class customerform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=customer

class bookingform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=booking

class subscribeform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=subscribe

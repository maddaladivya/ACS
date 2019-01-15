from django import forms
from django.contrib.auth.models import User
from StudentLogin.models import Tickets

class UserForm(forms.ModelForm):
    username = forms.CharField(help_text='Enter your last name',
                                widget=forms.TextInput(attrs={'placeholder': 'Username'}), required=False)
    email = forms.EmailField(help_text='Enter your email id',
                             widget=forms.EmailInput(attrs={'placeholder': 'Mail id'}), required=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class TicketForm(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = ('courierid', 'user')

from django import forms
from .models import Callback
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CallbackForm(forms.ModelForm):
    class Meta:
        model = Callback
        fields = ['name', 'phone', 'email', 'message']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'phone_number', 'is_superuser', 'bio', 'birthdate')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'phone_number', 'is_superuser', 'bio', 'birthdate')

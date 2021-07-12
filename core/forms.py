from django import forms
from django.contrib.auth.forms import UserCreationForm


#podemos crear un formulario para inyectarlo en la página web de registro
class CustomUserCreationForm(UserCreationForm):
    pass
from django.forms import ModelForm
from .models import Todo

class TodoUpdate(ModelForm):
    class Meta:
        model=Todo
        fields=['title','day']


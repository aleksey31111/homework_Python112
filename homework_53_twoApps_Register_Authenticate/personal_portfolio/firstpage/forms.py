from django.forms import ModelForm
from .models import Firstpage


class TodoForm(ModelForm):
    class Meta:
        model = Firstpage
        fields = ['title', 'description', 'image']  #, 'important']
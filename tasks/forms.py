from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new Task....'}))
    # complete = forms.BooleanField(widget=forms.RadioSelect)

    class Meta:
        model = Task
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field == 'complete':
                self.fields[field].widget.attrs.update({
                    'class':'form-check-input',
                })
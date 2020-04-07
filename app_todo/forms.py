from django import forms
from .models import List

# craeting List Model Form
class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['item','completed']

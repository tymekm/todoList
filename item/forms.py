from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'body', 'deadline', 'priority']
        lables = {'body': ''}
        widgets = {'event_date': forms.DateInput(
            attrs={'class': 'datepicker'})}

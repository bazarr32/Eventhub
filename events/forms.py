from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    date = forms.DateTimeField(
        input_formats=['%d.%m.%Y %H:%M', '%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={'placeholder': '04.09.2026 18:30'})
    )

    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'date', 'capacity', 'categories']
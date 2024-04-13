from django import forms
from django.forms import ModelForm
from notes.models import Note

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['summary','text','tags']


class SearchForm(forms.Form):
    search_summary = forms.CharField(label="Search for...", max_length=128)
    



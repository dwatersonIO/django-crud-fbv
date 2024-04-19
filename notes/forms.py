from django import forms
from django.forms import ModelForm
from notes.models import Note, Tag

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['summary','text','tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple
        }

class NoteSearchForm(forms.Form):
    summary = forms.CharField(required=False)
    text = forms.CharField(required=False)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)      


# class SearchForm(forms.Form):
#     search_summary = forms.CharField(label="Search for...", max_length=128)
    



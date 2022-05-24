from django import forms
from Notes.models import Note


class NoteCreateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']

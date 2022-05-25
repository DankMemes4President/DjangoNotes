from django import forms
from Notes.models import Note, Tag


class NoteCreateForm(forms.ModelForm):
    tag = forms.CharField(max_length=100)

    class Meta:
        model = Note
        fields = ['title', 'content', 'tag']

    def save(self, commit=True, **kwargs):
        form = super(NoteCreateForm, self).save(commit=False)
        tags = list(self.cleaned_data['tag'].split(','))

        if commit:
            form.save()
            for tag in tags:
                Tag.objects.create(title=tag, note=form)
        return form

class TagCreateForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title']

    def save(self, commit=True, **kwargs):
        form = super(TagCreateForm, self).save(commit=False)
        form.note = kwargs['pk']
        if commit:
            form.save()
        return form

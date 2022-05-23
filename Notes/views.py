from django.shortcuts import render
from django.views.generic import ListView
from Notes.models import Note, Tag


class NotesListView(ListView):
    model = Note
    template_name = 'Notes/index.html'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user']

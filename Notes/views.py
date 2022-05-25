from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from Notes.models import Note, Tag
from Notes.forms import NoteCreateForm


class UserLoginView(LoginView):
    template_name = 'Notes/login.html'


class NotesListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'Notes/index.html'
    paginate_by = 10

    def get_context_data(self, *, object_list=Note.get_notes_by_user, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['notes'] = self.object_list
        return context


class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'Notes/detail.html'

    def get_queryset(self, **kwargs):
        pk = self.kwargs['pk']
        return self.request.user.userprofile.note_set.filter(id=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = self.object.tag_set.all()
        return context


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'Notes/note_create.html'
    form_class = NoteCreateForm
    success_url = reverse_lazy('notes:list_notes')

    def form_valid(self, form):
        form.instance.user = self.request.user.userprofile
        # print(form.instance.user)
        return super().form_valid(form)


class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'Notes/delete.html'
    success_url = reverse_lazy('notes:list_notes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['note'] = self.object
        return context


class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    template_name = 'Notes/note_create.html'
    form_class = NoteCreateForm
    success_url = reverse_lazy('notes:list_notes')


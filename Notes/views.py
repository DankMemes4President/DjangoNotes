from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from Notes.models import Note, Tag


class UserLoginView(LoginView):
    template_name = 'Notes/login.html'

#class UserLogout(LogoutView)
#    template_name =


class NotesListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'Notes/index.html'
    paginate_by = 10

    def get_context_data(self, *, object_list=Note.get_notes_by_user, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['notes'] = self.object_list
        return context

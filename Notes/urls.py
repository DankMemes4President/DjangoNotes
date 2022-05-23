from django.urls import path
from Notes import views

app_name = "notes"

urlpatterns = [
    path('login', views.LoginView.as_view(template_name='Notes/login.html'), name='notes_login'),
    path('logout', views.LogoutView.as_view(template_name='Notes/logout.html'), name='notes_logout'),
    path('list', views.NotesListView.as_view(), name='list_notes'),
]
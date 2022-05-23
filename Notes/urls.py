from django.urls import path
from Notes import views

app_name = "notes"

urlpatterns = [
    path('list', views.NotesListView.as_view(), name='list_notes'),
]
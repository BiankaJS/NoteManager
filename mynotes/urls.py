from . import views
from django.urls import path

app_name="mynotes"

urlpatterns = [
  path("", views.list_notes, name="list_notes"),
  path("new/", views.new_note, name="new_note"),
  path("<int:note_id>", views.detail, name="detail"),
  path("<int:note_id>/edit/", views.modify_note, name="modify_note"),
  path("<int:note_id>/delete/", views.delete_note, name="delete_note")
]
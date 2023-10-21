from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from django.utils import timezone

#Metodo de consulta de todas las notas
def list_notes(request):
  notes_list = Note.objects.all()
  context = {
    "notes_list" : notes_list
  }
  return render(request, "mynotes/note_list.html", context)

#Metodo de creacion de una nota nueva 
def new_note(request):
  try:
    if request.method == 'POST':
      title = request.POST['title']
      content = request.POST['content']
      note = Note.objects.create(title = title, content = content, creation_date = timezone.now())
      return redirect('mynotes:detail', note.id)
    else:
      #Banderita para modificar la visualizacion del template
      return render(request, 'mynotes/note_edit.html', {"flag": False})
  except:
    return render(request, 'mynotes/note_edit.html', {"error_message" : "Ocurred an error"})

#Metodo de consulta de un nota por su id
def detail(request, note_id):
  note = get_object_or_404(Note, pk=note_id)
  return render(request, "mynotes/note_detail.html", {"note" : note})

#Metodo de modificacion de una nota por su id
def modify_note(request, note_id):
  try:
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
      note. title = request.POST['title']
      note.content = request.POST['content']
      note.save()
      return redirect('mynotes:detail', note.id)
    else:
      #Banderita para modificar la visualizacion del template
      return render(request, 'mynotes/note_edit.html', {"note": note, "flag": True})
  except:
    return redirect('mynotes:list_notes')

#Metodo de eliminacion de una nota por id
def delete_note(request, note_id):
  note = get_object_or_404(Note, pk=note_id)
  note.delete()
  return redirect('mynotes:list_notes')



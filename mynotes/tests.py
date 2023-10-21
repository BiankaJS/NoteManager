from django.urls import reverse
from django.utils import timezone
from django.test import TestCase
from .models import Note

class NoteModelTests(TestCase):
  def test_create_new_note(self):
    url = reverse('mynotes:new_note')
    self.client.post(url, {'title': 'Prueba de notita', 'content': 'Este es el contenido de la nota'})

    new_note = Note.objects.first()
    self.assertEqual(Note.objects.count(), 1)
    self.assertEqual(new_note.title, 'Prueba de notita')
    self.assertEqual(new_note.content, 'Este es el contenido de la nota')

  def test_modify_note(self):
    note = Note(title = 'Nota de prueba', content= 'Este es el contenido principal', creation_date = timezone.now())
    note.save()

    url = reverse('mynotes:modify_note', args=[note.id])
    response = self.client.post(url, {'title': 'Título Modificado', 'content': 'Contenido Modificado'})

    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, reverse('mynotes:detail', args=[note.id]))
    note.refresh_from_db()
    self.assertEqual(note.title, 'Título Modificado')
    self.assertEqual(note.content, 'Contenido Modificado')

  def test_delete_note(self):
    note = Note.objects.create(title = 'Nota de prueba', content= 'Este es el contenido principal', creation_date = timezone.now())
    url = reverse('mynotes:delete_note', args=[str(note.id)])
    response = self.client.post(url)

    self.assertEqual(response.status_code, 302)
    with self.assertRaises(Note.DoesNotExist):
      Note.objects.get(pk=note.id)

  def test_get_detail_note(self):
    note = Note.objects.create(title = 'Nota de prueba', content= 'Este es el contenido principal', creation_date = timezone.now())
    url = reverse('mynotes:detail', args=[str(note.id)])
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Nota de prueba")

  def test_load_list_notes(self):
    Note.objects.create(title = 'Nota de prueba', content= 'Este es el contenido principal', creation_date = timezone.now())
    Note.objects.create(title = 'Nota de prueba 02', content= 'Este es el contenido principal 02', creation_date = timezone.now())
    Note.objects.create(title = 'Nota de prueba 03', content= 'Este es el contenido principal 03', creation_date = timezone.now())

    url = reverse('mynotes:list_notes')
    response = self.client.get(url)

    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'Nota de prueba')
    self.assertContains(response, 'Nota de prueba 02')
    self.assertContains(response, 'Nota de prueba 03')

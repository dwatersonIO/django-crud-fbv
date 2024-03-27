from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Note
from .forms import NoteForm

def index(request):
	notes = Note.objects.all().order_by('-date_created')

	form = NoteForm()

	if request.method =='POST':
		form = NoteForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')


	context = {'notes':notes, 'form':form}
	return render(request, 'notes/index.html', context)

def update_note(request, pk):
	note = Note.objects.get(id=pk)

	form = NoteForm(instance=note)

	if request.method == 'POST':
		form = NoteForm(request.POST, instance=note)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'notes/update_note.html', context)

def delete_note(request, pk):
	note = Note.objects.get(id=pk)

	if request.method == 'POST':
		note.delete()
		return redirect('/')

	context = {'note':note}
	return render(request, 'notes/delete_note.html', context)

def search_note(request):
	if request.method == "POST":
		form=NoteForm(request.POST)
		if form.is_valid():
			searched=form.cleaned_data["text"]
			notes = Note.objects.filter(text__contains=searched)	

	else:
		notes = Note.objects.all().order_by('-date_created')
		form=NoteForm()
		
	return render(request, 'notes/search_note.html', {"form": form, "notes": notes})


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

def create_note(request):

	form = NoteForm()

	if request.method =='POST':
		form = NoteForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')

	context = {'form':form}
	return render(request, 'notes/create_note.html', context)

def update_note(request, pk):
	note = Note.objects.get(id=pk)

	if request.method == 'POST':
		form = NoteForm(request.POST, instance=note)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = NoteForm() # GET Request returns empty form

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
			form=NoteForm()	

	else:
		notes = Note.objects.all().order_by('-date_created')
		form=NoteForm()
		searched=""


	return render(request, 'notes/index.html', {"form": form, "notes": notes, "searched": searched})


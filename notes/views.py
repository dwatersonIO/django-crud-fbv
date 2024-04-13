from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Note
from .forms import NoteForm, SearchForm

def index(request):
	notes = Note.objects.all().order_by('-date_created') # order_by not needed since order in Model Meta field

	context = {'notes':notes}
	return render(request, 'notes/index.html', context)


def detail_note(request, pk):
	note = Note.objects.get(id=pk)

	if request.method == 'POST':
		form = NoteForm(request.POST, instance=note)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = NoteForm() # GET Request returns empty form

	context = {'note': note, 'form':form}
	return render(request, 'notes/detail_note.html', context)

def create_note(request):

	form = NoteForm()

	if request.method =='POST':
		form = NoteForm(request.POST)
		print (form)
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
		form = NoteForm(instance=note) # if Get request just show current data

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
		form=SearchForm(request.POST)
		if form.is_valid():
			searched=form.cleaned_data["search_summary"]
			notes = Note.objects.filter(summary__contains=searched)
			form=SearchForm()	

	else:
		notes = Note.objects.all().order_by('-date_created')
		form=SearchForm()
		# form.fields['tags'].required = False  # Set tags field as optional for search view
		# form.fields['text'].required = False  # Set tags field as optional for search view
		searched=""


	return render(request, 'notes/search_note.html', {"form": form, "notes": notes, "searched": searched})

# def search_note(request):
# 	if request.method == "POST":
# 		form=NoteForm(request.POST)
# 		if form.is_valid():
# 			searched=form.cleaned_data["summary"]
# 			notes = Note.objects.filter(summary__contains=searched)
# 			form=NoteForm()	

# 	else:
# 		notes = Note.objects.all().order_by('-date_created')
# 		form=NoteForm()
# 		# form.fields['tags'].required = False  # Set tags field as optional for search view
# 		# form.fields['text'].required = False  # Set tags field as optional for search view
# 		searched=""


# 	return render(request, 'notes/search_note.html', {"form": form, "notes": notes, "searched": searched})


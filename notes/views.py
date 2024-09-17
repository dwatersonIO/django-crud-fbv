from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Note, Tag
from .forms import NoteForm, NoteSearchForm, TagForm

def index(request):
	notes = Note.objects.prefetch_related("tags").order_by('-date_created') # order_by not needed since order in Model Meta field
	# Better than Note.objects.all() since avoids n+1 problem. ie template issuing multiple sql queries to find the many-to-many queries
	# If the relationship is one to many then use "select_related." "prefetch_related" used on many to many relationships.
 
 
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
	tags = Tag.objects.all()
	if request.method =='POST':
		form = NoteForm(request.POST)
		print (form)
		if form.is_valid():
			form.save()
		return redirect('/')

	context = {'form':form,'tags':tags}
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
	if request.method == 'POST':

		form=NoteSearchForm(request.POST)
		
		if form.is_valid():
			summary=form.cleaned_data["summary"]
			text = form.cleaned_data["text"]
			tags = form.cleaned_data["tags"]

		# Start with an empty queryset
		notes = Note.objects.all()

		# Filter based on submitted data
		if summary:
			notes = notes.filter(summary__icontains=summary)
		if text:
			notes = notes.filter(text__icontains=text)
		if tags:
			notes = notes.filter(tags__in=tags)
			
		form=NoteSearchForm()	

	else:
		notes = Note.objects.all().order_by('-date_created')
		form=NoteSearchForm()
		
	return render(request, 'notes/search_note.html', {"form": form, "notes": notes})

def create_tag(request):

	form = TagForm()
	tags = Tag.objects.all()
	
	if request.method =='POST':
		form = TagForm(request.POST)
		
		if form.is_valid():
			form.save()
		return redirect('/')

	context = {'form':form,'tags':tags}
	return render(request, 'notes/create_tag.html', context)


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Note
# Create your views here.
def indexview(request):
    notes = Note.objects.all()
    return render(request, 'index.html', context={'notes':notes})

def aboutview(request):
    return render(request, 'about.html')

def savedataview(request):
    print(request.POST)
    title = request.POST.get('title',"")
    description = request.POST.get('description',"")

    if not title or not description:
        messages.error(request, "Fill all details")
        return redirect("/")
    note = Note(title=title, description = description)
    note.save()
    messages.success(request, 'data saved successfully')
    return redirect('/')

def deleteview(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    messages.success(request, 'note deleteed')
    return redirect('/')


def updateviewpage(request, id):
    note = Note.objects.get(id=id)

    if request.method == 'POST':
        title = request.POST.get('title',"")
        description = request.POST.get('description',"")
        if not title or not description:
            messages.error(request, "Fill all details")
        note.title = title
        note.description = description
        note.save()
        messages.success(request, 'note updated successfully')
        return redirect('/')

    return render(request, 'edite_page.html', context={'note': note})
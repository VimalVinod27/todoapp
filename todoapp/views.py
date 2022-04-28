from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .forms import TodoUpdate

from .models import Todo

# Create your views here.
def home(request):
    obj=Todo.objects.all()

    if request.method=='POST':
        title=request.POST.get('title')
        date=request.POST.get('date')
        if date!="":

            Todo.objects.create(title=title,day=date)
        else:
            Todo.objects.create(title=title)


    return render(request,'home.html',{'obj':obj})

def delete(request,id):
    obj=get_object_or_404(Todo,id=id)
    obj.delete()
    return redirect('home')
def complete(request,id):
    obj=get_object_or_404(Todo,id=id)
    obj.complete=True
    obj.save()
    return redirect('home')
def update(request,id):
    obj=Todo.objects.get(pk=id)
    if request.method=='POST':
        form=TodoUpdate(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('home')

    form=TodoUpdate(instance=obj)
    return render(request,'todo_update_form.html',{'form':form,'obj':obj})




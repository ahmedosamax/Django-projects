from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProjectForm
from .models import project

def projects(request):
    projects = project.objects.all()
    context = {"projects":projects}
    return render(request,'projects/projects.html',context)

def pproject(request,pk):
    projectObj = project.objects.get(id = pk)
    context = {'project':projectObj}
    return render(request,'projects/project.html',context)

def CreateProject(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

def updateProject(request,pk):
    proj = project.objects.get(id=pk)
    form = ProjectForm(instance = proj)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance= proj)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

def deleteProject(request, pk):
    proj = project.objects.get(id = pk)
    if request.method == "POST":
        proj.delete
        return redirect("projects")
    context = {'object':proj}
    return render (request,projects/'delete_template.html',context)
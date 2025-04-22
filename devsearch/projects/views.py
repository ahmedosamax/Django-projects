from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from django.contrib import messages
from .models import project

def projects(request):
    projects = project.objects.all()
    context = {"projects":projects}
    return render(request,'projects/projects.html',context)

def pproject(request,pk):
    projectObj = project.objects.get(id = pk)
    context = {'project':projectObj}
    return render(request,'projects/project.html',context)

@login_required(login_url= 'login')
def CreateProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit = False)
            project.owner = profile
            project.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url= 'login')
def updateProject(request,pk):
    profile = request.user.profile
    proj = profile.project_set.get(id=pk)
    form = ProjectForm(instance = proj)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance= proj)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url= 'login')
def deleteProject(request, pk):
    profile = request.user.profile
    proj = profile.project_set.get(id=pk)
    if request.method == "POST":
        proj.delete()
        return redirect("account")
    context = {'object':proj}
    return render (request,'delete_template.html',context)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm,ReviewForm
from django.contrib import messages
from .models import project

from .utils import searchProject,paginationProject




def projects(request):
    projects,search_query = searchProject(request)
    custom_range,projects = paginationProject(request,projects,2)

    context = {"projects":projects, 'search_query': search_query , 'custom_range':custom_range}
    return render(request,'projects/projects.html',context)

def pproject(request,pk):
    projectObj = project.objects.get(id = pk)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.Project = projectObj
        review.owner = request.user.profile
        review.save()
        projectObj.getVoteCount
        messages.success(request,'Your review was successfuly submitted!')
        return redirect('project',pk=projectObj.id)
    context = {'project':projectObj,'form':form}
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
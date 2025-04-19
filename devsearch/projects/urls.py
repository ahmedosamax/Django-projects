from django.urls import path
from . import views

urlpatterns = [
    path('',views.projects, name = 'projects'),
    path('project/<uuid:pk>/',views.pproject, name = 'project'),
    path('create-project/', views.CreateProject, name = 'create-project'),
    path('update-project/<str:pk>/', views.updateProject, name = 'update-project'),
    path('delete-project/<str:pk>/', views.deleteProject, name = 'delete-project'),
]
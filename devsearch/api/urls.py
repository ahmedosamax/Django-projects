from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns= [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('',views.getRoutes),
    path('projects/',views.getProjects),
    path('projects/<str:pk>/',views.getProject),
    path('projects/<str:pk>/vote/',views.projectVote),
    path('remove-tag/',views.removeTag)
    
]
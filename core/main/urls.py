from django.urls import path

# custom
from . import views


urlpatterns = [
    path('projects/', views.ProjectAPIView.as_view()),
    path('tasks/', views.TaskAPIView.as_view()),
]
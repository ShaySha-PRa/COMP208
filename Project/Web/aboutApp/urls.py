from django.urls import path
from . import views

app_name = 'aboutApp'

urlpatterns = [
    path('survey/', views.survey, name='survey'),  # Introduction 
    path('honor/', views.honor, name='honor'),     # Honor
]
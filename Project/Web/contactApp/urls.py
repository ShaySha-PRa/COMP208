from django.urls import path
from . import views

app_name = 'contactApp'

urlpatterns = [
    path('contact/', views.contact, name='contact'),    # Contact us
    path('recruit/', views.recruit, name='recruit'),    # Join us
]
from django.urls import path
from . import views

app_name = 'newsApp'

urlpatterns = [
    path('news/<str:newName>/', views.news, name='news'),#News列表
    path('newDetail/<int:id>/', views.newDetail, name='newDetail'),#News详情
    path('search/', views.search, name='search'),#News搜索
]
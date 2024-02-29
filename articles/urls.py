from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ViewArticles),
    path('create', views.CreateArticles)
]
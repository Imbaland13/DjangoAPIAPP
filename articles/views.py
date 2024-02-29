from django.shortcuts import render
from django.http import JsonResponse
from .models import Article 
# Create your views here.

def WelcomePage(response):
    return render(response, 'home.html')

def ViewArticles(response):
    data = list(Article.objects.values())
    return JsonResponse({'articles': data})

def CreateArticles(response):
    articles1 = Article.objects.create(headline = "test", text = "blablabla", author = "Daniel Tesch")
    articles2 = Article.objects.create(headline = "test2", text = "blog", author = "Influencer")
    articles3 = Article.objects.create(headline = "test3", text = "yaddayaddayadda", author = "AnnoyingAdCompany")
    return render(response, 'create.html')

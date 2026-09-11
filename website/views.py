from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index_view(request):
    return HttpResponse("<h1> this is homePage </h1>")

def about_view(request):
    return HttpResponse("<h1> this is AboutPage </h1>")

def contact_view(request):
    return HttpResponse("<h1> this is ContactPage </h1>")


from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def post_create(request):
    return HttpResponse("<h1>Create<h1/>")


def post_create(request):
    return HttpResponse("<h1>Create<h1/>")



def post_home(request):
	return HttpResponse("<h1>Hello</h1>")

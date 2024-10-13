from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'website/index.html')

def about(request):
    return HttpResponse("HEllo world at chai aur dango home page")

def contact(request):
    return HttpResponse("HEllo world at chai aur dango home page")

from django.shortcuts import render, redirect

from django.http import HttpResponse, JsonResponse
from .forms import *
from .models import *
def index(request):
    return render(request,"default.html")

def register(request):
    if request.method == 'POST':
        form = registration_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("/")
    else:
        form = registration_form()
    context = {"form":form}
    return render(request,"register.html",context)

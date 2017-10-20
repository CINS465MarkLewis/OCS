from django.shortcuts import render, redirect

from django.http import HttpResponse, JsonResponse
from .forms import *
from .models import *
# Create your views here.
def index(request):
    #return HttpResponse("CINS465 Hello World")
    if request.method == 'POST':
        form = suggestion_form(request.POST)
        if form.is_valid():
            modentry = suggestion(suggestion=form.cleaned_data['suggestion'])
            modentry.save()
    else:
        form = suggestion_form()
    suggestions = suggestion.objects.all()
    context = {"variable":suggestions, "form":form}
    return render(request,"default.html", context, form)
    
def register(request):
    if request.method == 'POST':
        form = registeration_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("/")
        else:
            form = registration_form()
        context = {"form":form}
        return render(request,"register.html",context)

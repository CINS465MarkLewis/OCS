from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.http import Http404
from .forms import *
from .models import *

def index(request):
    all_universities = University.objects.all()
    template = loader.get_template('base.html')
    context = {
        'all_universities': all_universities
    }
    return render(request, "base.html", context)

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

def detail(request, university_id):
    try:
        test = University.objects.get(pk=university_id)
    except University.DoesNotExist:
        raise Http404("University ID does not exist")
    return render(request, "org.html", {'test': test})

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from django.http import Http404
from mysite import settings
from .forms import *
from .models import *
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class IndexView(generic.ListView):
    template_name = "index.html"

    def get_queryset(self):
        return University.objects.all()

class OrgIndex(generic.ListView):
    model = Org
    template_name = "org_index.html"

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

class DetailView(generic.DetailView):
    model = University
    context_object_name= 'test'
    template_name = "org.html"

class UniversityCreate(CreateView):
    model = University
    template_name = "university_form.html"
    fields = ['uniName', 'uniLogo', 'uniLoca']

class OrgCreate(CreateView):
    model = Org
    #reUsed uni form to reduce code
    template_name = "university_form.html"
    fields = ['orgName', 'orgLogo', 'orgFoun', 'orgCateg']

def home(request):
    c = Chat.objects.all()
    return render(request, "croom.html", {'croom': 'active', 'chat': c})

def post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        c = Chat(user=request.user, message=msg)
        if msg != '':
            c.save()
        return JsonResponse({ 'msg':msg, 'user':c.user.username })
    else:
        return HttpResponse("Messsged")

def Messages(request):
    c = Chat.objects.all()
    return render(request, 'messages.html', {'chat': c})

def voteIndex(request):
    latest_questions = Question.objects.order_by("-date")[:5]
    context = {'latest_questions': latest_questions}
    return render(request, 'polls/poll.html',context)

def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'polls/detail.html',{"question": question_id})

def results(request, question_id):
    return HttpResponse("results %s" % question_id)

def vote(request, question_id):
    return HttpResponse("Vote on question %s" % question_id)

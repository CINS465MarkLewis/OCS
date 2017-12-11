from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import loader
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

def vote(request):
   thread_id = int(request.POST.get('id'))
   vote_type = request.POST.get('type')
   vote_action = request.POST.get('action')

   thread = get_object_or_404(Thread, pk=thread_id)

   thisUserUpVote = thread.userUpVotes.filter(id = request.user.id).count()
   thisUserDownVote = thread.userDownVotes.filter(id = request.user.id).count()

   if (vote_action == 'vote'):
      if (thisUserUpVote == 0) and (thisUserDownVote == 0):
         if (vote_type == 'up'):
            thread.userUpVotes.add(request.user)
         elif (vote_type == 'down'):
            thread.userDownVotes.add(request.user)
         else:
            return HttpResponse('error-unknown vote type')
      else:
         return HttpResponse('error - already voted', thisUserUpVote, thisUserDownVote)
   elif (vote_action == 'recall-vote'):
      if (vote_type == 'up') and (thisUserUpVote == 1):
         thread.userUpVotes.remove(request.user)
      elif (vote_type == 'down') and (thisUserDownVote ==1):
         thread.userDownVotes.remove(request.user)
      else:
         return HttpResponse('error - unknown vote type or no vote to recall')
   else:
      return HttpResponse('error - bad action')


   num_votes = thread.userUpVotes.count() - thread.userDownVotes.count()

   return HttpResponse(num_votes)

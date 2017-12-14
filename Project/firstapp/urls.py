from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'org/list/$', views.OrgIndex.as_view(), name='org-index'),
    url(r'register/$',views.register, name='register'),
    url(r'croom/$',views.home, name='croom'),
    url(r'poll/$',views.voteIndex, name='voteIndex'),
    url(r'^(?P<question_id>[0-9]+)/detail$', views.detail, name='vote_detail'),
    url(r'^(?P<question_id>[0-9]+)/results$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name='vote'),
    url(r'university/add/$', views.UniversityCreate.as_view(), name='university-add'),
    url(r'org/add/$', views.OrgCreate.as_view(), name='org-add')
]

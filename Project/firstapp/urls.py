from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'register/$',views.register, name='register'),
    url(r'croom/$',views.home, name='croom'),
    url(r'post/$',views.post, name='post'),
    url(r'messages/$',views.Messages, name='messages'),
    url(r'vote/$',views.vote,name='vote'),
    #1,2 or university id
    #url(r'^(?P<university_id>[0-9]+)/$', views.detail, name='detail')
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'university/add/$', views.UniversityCreate.as_view(), name='university-add')
]

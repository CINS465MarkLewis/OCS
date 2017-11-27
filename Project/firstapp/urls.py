from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'register/$',views.register, name='register'),
    url(r'croom/$',views.home, name='croom'),
    url(r'post/$',views.post, name='post'),
    url(r'messages/$',views.Messages, name='message'),
    #url(r'vote/$',views.vote, name='vote'),
    #1,2 or university id
    url(r'^(?P<university_id>[0-9]+)/$', views.detail, name='detail')
]

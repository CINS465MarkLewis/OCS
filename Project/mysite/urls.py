from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from firstapp.forms import LoginForm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'login/$', views.login, {
        'template_name':'login.html',
        'authentication_form':LoginForm
    }, name="login"),
    url(r'logout/$', views.logout,{
        'next_page':'/login'
    }),
    url(r'',include('firstapp.urls')),
    ]

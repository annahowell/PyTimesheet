from . import views

from django.conf.urls import url
from django.contrib import admin

from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login', ),
    url(r'^logout/$', auth_views.logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view()),
]

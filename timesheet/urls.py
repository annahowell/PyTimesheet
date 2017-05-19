from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from ts_app import views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login', ),
    url(r'^logout/$', auth_views.logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.entry.EntryIndexView.as_view(), name='entry'),
    url(r'^employee/$', views.employee.IndexView.as_view(), name='employee'),
    url(r'^project/$', views.project.IndexView.as_view(), name='project'),
]

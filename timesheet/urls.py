from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from timesheet_app import views

urlpatterns = [
    url(r'^$', login_required(views.entry.IndexView.as_view()), name='entry'),

    url(r'^employee/$', login_required(views.employee.IndexView), name='employee'),
    url(r'^ajax/validate_username/$', login_required(views.validate_username), name='validate_username'),

    url(r'^project/$', login_required(views.project.IndexView), name='project'),

    url(r'^client/$', login_required(views.client.IndexView), name='client'),
    url(r'^report/$', login_required(views.report.IndexView), name='report'),

    #url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'employee_login.html'}, name='login'),
    url(r'^logout/$', login_required(auth_views.logout), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]

from django.conf.urls import url

from . import views

app_name = 'employee'
urlpatterns = [
    #url(r'^$', views.IndexView, name='index'),
    url(r'^new/$', views.post_new, name='post_new'),

]
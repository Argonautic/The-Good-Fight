from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.choices, name='choices'),
    url(r'^(?P<action_id>\d+)', views.detail, name='detail'),
    url(r'^(?P<timespan>\w+_Actions)', views.choiceActions, name='choiceActions'),
    url(r'^index', views.index, name='index'),
]
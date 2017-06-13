from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.choices, name='choices'),
    url(r'^(?P<action_id>\d+)', views.detail, name='detail'),
    url(r'^shortActions', views.shortActions, name='shortActions'),
    url(r'^mediumActions', views.mediumActions, name='mediumActions'),
    url(r'^longActions', views.longActions, name='longActions'),
    url(r'^index', views.index, name='index'),
]
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from login import views as login_views

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^signup', login_views.signup, name='signup'),
    url(r'^user_login', login_views.user_login, name='user_login'),
    url(r'^user_logout', login_views.user_logout, name='user_logout'),
    url(r'^login_successful', login_views.login_successful, name='login_successful'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^password', include('login.urls')),
    url(r'^', include('changeActions.urls')),
]

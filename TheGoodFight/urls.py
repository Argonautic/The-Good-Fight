from django.conf.urls import include, url
from django.contrib import admin
from login import views as login_views

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^signup', login_views.signup, name='signup'),
    url(r'^user_login', login_views.user_login, name='user_login'),
    url(r'^user_logout', login_views.user_logout, name='user_logout'),
        url(r'^password_reset', login_views.password_reset, name='password_reset'),
    url(r'^', include('changeActions.urls')),
]

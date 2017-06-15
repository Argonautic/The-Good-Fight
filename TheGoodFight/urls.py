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
    url(r'^password_reset$', auth_views.PasswordResetView.as_view(   template_name='login/password_reset_form.html', email_template_name='login/password_reset_email.html', subject_template_name='login/password_reset_subject.txt'), name='password_reset'),
    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})', auth_views.PasswordResetConfirmView.as_view(template_name='login/password_reset_confirm.html'), name='password_reset_confirm'),
    url(r'^password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name='login/password_reset_done.html'), name='password_reset_done'),
    url(r'^password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name='login/password_reset_complete.html'), name='password_reset_complete'),
    url(r'^', include('changeActions.urls')),
]

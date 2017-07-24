from django.conf.urls import url  # , include
from django.contrib.auth import views as auth_views
from login import views
urlpatterns = [
    url('^$', views.home, name='home'),
    url('^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url('^logout/$', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    url('^password_change/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    url('^password_change/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    url('^password_reset/$', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    url('^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    url('^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    url('^reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]


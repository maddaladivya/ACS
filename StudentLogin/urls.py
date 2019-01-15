from django.conf.urls import url, include
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from StudentLogin import views
from cir1 import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^home/$', views.home.as_view(), name="home"),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', auth_views.login, {'template_name': 'StudentLogin/login.html'}, name='login'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^logout/$', auth_views.logout, name="logout"),
    url(r'^index/$', views.index.as_view(), name="index"),
    url(r'^(?P<pk>\d+)/$', views.ProfileDetailView.as_view(), name="profile"),
    url(r'^ticket/$', views.Ticket.as_view(), name="ticket"),
]

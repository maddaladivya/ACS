from django.conf.urls import url, include
from django.conf.urls.static import static
from courier import views

urlpatterns = [
    url(r'^home/$', views.home.as_view(), name="home"),
    url(r'^order/$', views.Order.as_view(), name="order"),
]

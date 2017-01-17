from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'process_new/', views.process_new, name='process_new'),
]

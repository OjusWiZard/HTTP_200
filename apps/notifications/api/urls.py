from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^set_firebase_token/$', views.set_firebase_token, name='set_firebase_token'),
]

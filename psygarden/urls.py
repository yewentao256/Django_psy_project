from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = "psygarden"
urlpatterns = [
    url(r"psygardenList/", views.psygardenList),
    url(r"comment/", views.comment),
    url(r"mood_message/", views.mood_message),
]
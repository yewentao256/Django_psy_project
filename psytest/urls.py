from django.urls import path
from django.conf.urls import url, include
from . import views
app_name = "psytest"
urlpatterns = [
    url(r"getTestQuestions/", views.getTestQuestions),
    url(r"uploadTest/", views.uploadTest),
]

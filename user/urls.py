from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = "user"
urlpatterns = [
    url(r"login/", views.login),
    url(r"register/", views.register),
    url(r"updatePass/", views.updatePass),
    url(r"editUserInfo/", views.editUserInfo),
    url(r"getUserInfo/", views.getUserInfo),
    url(r"verifyUser/", views.verifyUser),
    url(r"consultantList/", views.consultantList),
]
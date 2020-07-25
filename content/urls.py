from django.urls import path
from django.conf.urls import url, include
from . import views
app_name = "content"
urlpatterns = [
    url(r"upload_file/", views.upload_file),
]

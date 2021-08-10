from django.urls import path
from .views import *



app_name = "post"



urlpatterns = [
    path("", posts, name="posts"),
    path("create", posts_create, name="create"),
    path("<slug>", posts_detail, name="detail"),
    path("<slug>/update", posts_update, name="update"),
    path("<slug>/delete", posts_delete, name="delete"),
]
from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[
    path("", views.index,name="main"),
    path("add/", views.add, name="add"),
    path("update/<int:id>", views.update, name="update"),
    path("detail/<int:id>", views.detail,name="detail"),
    path("delete/<int:id>", views.delete,name="delete"),
    path("onOff/", views.onOff,name="like_post"),
]

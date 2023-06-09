from django.urls import path,include
from .views import home,user_data,face_search,person_details

urlpatterns=[
    path("",home,name="home"),
    path("user_data",user_data,name="user_data"),
    path("face_search",face_search,name="face_search"),
    path("person_details",person_details,name="person_details"),
]

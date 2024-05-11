from django.contrib import admin
from django.urls import path

from . import views

app_name = "lessons"

urlpatterns = [
    path('<int:id>/', views.view_course),
    path('<int:id>/video', views.lesson_video),
    path('<int:id>/stream', views.rtmp_stream),
]

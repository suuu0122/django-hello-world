from django.urls import path

from . import views



app_name = "hello_world_app"
urlpatterns = [
    path('hello_world_function', views.index, name="fucntion_index"),
    path('hello_world_class', views.IndexView.as_view(), name="class_index"),
]
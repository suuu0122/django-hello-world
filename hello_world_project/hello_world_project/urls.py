from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("hello_world_app.urls")),
]
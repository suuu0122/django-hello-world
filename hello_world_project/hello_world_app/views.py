from django.http import HttpResponse
from django.views.generic import TemplateView


def index(request):
    response = HttpResponse("<h1>Hello World!</h1>")
    return response



class IndexView(TemplateView):
    template_name = "hello_world_app/index.html"
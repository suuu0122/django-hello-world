from django.http import HttpResponse



def index(request):
    response = HttpResponse("<h1>Hello World!</h1>")
    return response
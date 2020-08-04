from django.http import HttpResponse


def index(req):
    return HttpResponse("Hello, world. Polls App is working correctly. Have Fun.")
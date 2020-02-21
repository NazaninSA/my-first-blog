from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Hello I'm view from main project")
from django.http import HttpResponse

def index(request):
    return HttpResponse("<H1>THIS IS THE MUSIC APP HOMEPAGE</H1>")

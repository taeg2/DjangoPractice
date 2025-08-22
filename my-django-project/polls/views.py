from django.http import HttpResponse

def index(requset):
    return HttpResponse("hello, world/ you're at the polls index.")
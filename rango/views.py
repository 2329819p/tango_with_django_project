

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, candy, cookie'}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return HttpResponse("Rango says here is about!")

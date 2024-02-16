from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Create your views here.

def blog(request):

    print('MINHA HOME')
    return HttpResponse('ESTE É O BLOG1')

def blog2(request):

    return HttpResponse('ESTE É O BLOG2 ')
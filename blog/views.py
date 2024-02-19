from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def blog(request):

    
    return render(request, 'bloga.html')

def blog2(request):

    return HttpResponse('ESTE É O BLOG2 ')
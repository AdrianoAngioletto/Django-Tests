from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def blog(request):


    variavel = 'olá mundo, DJANGO'

    
    return render(request,  'bloga.html', {'minha_variavel': variavel})

def blog2(request):

    return HttpResponse('ESTE É O BLOG2 ')
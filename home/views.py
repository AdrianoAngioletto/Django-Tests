from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test(request):

    print('MINHA HOME')
    return HttpResponse('NOVA NEW')

def nova(request):

    return HttpResponse('nova resposta')
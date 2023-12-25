from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic

def hello1(request):
    return HttpResponse('こんにちは')

def hello2(request):
    return render(request, 'hello2.html')

class Hello3View(generic.TemplateView):
    template_name = 'hello2.html'

def hello4(request):
    return redirect('ex2:hello1')


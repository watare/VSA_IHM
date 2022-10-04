from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band 

def hello(request):
    bands = Band.objects.all()
    return render(request,
    'listings/hello.html',
    {'bands': bands})

def about(request):
    return HttpResponse('<h1>On est des fous<h1><p>je crois que j\'ai la solution<p>')

def contact(request):
    return HttpResponse('<p>mon tel est le : 0652228442 <p>')
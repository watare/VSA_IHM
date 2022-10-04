from email import message
from django.http import HttpResponse
from django.shortcuts import redirect, render
from listings.models import Band
from listings.form import BandForm, ContactUsForm 
from django.core.mail import send_mail

def hello(request):
    bands = Band.objects.all()
    return render(request,
    'listings/hello.html',
    {'bands': bands})
    
def bandList(request):
    bands = Band.objects.all()
    return render(
        request,
        'listings/band_list.html',
        {'bands' : bands})
    
def bandDetail(request,id):
    band = Band.objects.get(id=id)
    return render(request,'listings/band_detail.html',{'band' : band})
    
def about(request):
    return HttpResponse('<h1>On est des fous<h1><p>je crois que j\'ai la solution<p>')

def contact(request):
    
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"}]',
                message= form.cleaned_data["message"],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()
        
        
    return render(request,'listings/contact.html',{'form':form})

def emailSent(request):
    return HttpResponse('<h1>email envoyé!</h1>')

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)  
    else:
        form = BandForm()
        
    return render(request,'listings/band_create.html',{'form' : form})
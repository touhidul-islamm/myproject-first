from django.shortcuts import render, redirect
#for get data form model.
from .models import Service, Testmonial, Feature, Portfolio, Banner, Newfeature
from .forms import ContactForm

from django.views.generic.base import TemplateView
# Create your views here.
def index(request):
    banner=Banner.objects.all()
    context={
        'banner':banner
    }
    return render(request, 'index.html', context)

def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
        
    else:
        form=ContactForm()
    context={
        'form':form
    }
    return render(request, 'contact.html', context)

def partner(request):
    return render(request, 'partner.html')

def testmonial(request):
    testmonial=Testmonial.objects.all()
    context={
        'testmonial':testmonial
    }
    return render(request, 'testimonials.html', context)

def latestnews(request):
    return render(request, 'latestnews.html')

def pricing(request):
    return render(request, 'pricing.html')

def team(request):
    return render(request, 'team.html')

# This is service section
def services(request):
    ser=Service.objects.all().order_by('ordering')
    context={
        'service':ser
    }

    return render(request, 'services.html', context)
# end service section

def about(request):
    return render(request, 'about.html')

def portfolio(request):
    portfolio=Portfolio.objects.all()
    context={
        'portfolio':portfolio
    }
    return render(request, 'portfolio.html', context)

def feature(request):
    feature=Feature.objects.all()
    newfeature=Newfeature.objects.last()
    context={
        'feature':feature,
        'newfeature':newfeature
    }
    return render(request, 'feature.html', context)

class Genview(TemplateView):
    template_name='newgeneric.html'
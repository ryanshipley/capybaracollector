# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from main_app.models import Capybara

# Define the home view
def home(request):
  return HttpResponse('<a href="about/"><h1>click here</h1></a>')

def about(request):
    return render(request, 'about.html')

def cap_index(request):
    capybaras = Capybara.objects.all()
    return render(request, 'capybaras/index.html', { 'capybaras' : capybaras })

def cap_detail(request, capybara_id):
    capybara = Capybara.objects.get(id=capybara_id)
    return render(request, 'capybaras/detail.html', { 'capybara' : capybara})

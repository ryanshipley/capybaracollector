# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from main_app.models import Capybara
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CleaningForm

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
    cleaning_form = CleaningForm()
    return render(request, 'capybaras/detail.html', { 'capybara' : capybara, 'cleaning_form' : cleaning_form})

class CapCreate(CreateView):
    model = Capybara
    fields = '__all__'
    success_url = '/capybaras/'

class CapUpdate(UpdateView):
    model = Capybara
    fields = ['color', 'description', 'age']
    success_url = '/capybaras/'

class CapDelete(DeleteView):
    model = Capybara
    success_url = '/capybaras/'

def add_cleaning(request, capybara_id):
    form = CleaningForm(request.POST)
    if form.is_valid():
        new_cleaning = form.save(commit=False)
        new_cleaning.capybara_id = capybara_id
        new_cleaning.save()
    return redirect('detail', capybara_id = capybara_id)
from django.shortcuts import reverse
from django.views import generic
from .form import *

class Home(generic.TemplateView):
    template_name = 'index.html'

class Succes(generic.TemplateView):
    template_name = 'registration/succes.html'
    
class Registration(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = Easy
    
    def get_success_url(self):
        return reverse('django:login')

class ChangeImage(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = Easy
    
    def get_success_url(self):
        return reverse('django:login')
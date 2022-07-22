from django.shortcuts import render, reverse
from django.views import generic
from .models import Admin
from .form import *

class Home(generic.TemplateView):
    template_name = 'index.html'
    
class Registration(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = Easy
    
    def get_success_url(self):
        return reverse('django:login')

def changeImage(request):
    if request.method == "POST":
        form = Img(request.POST)
        if form.is_valid():
            form.save()
            return reverse("django:home")
    else:
        form = Img()
    
    return render(request, 'change-user.html', {"form":form})
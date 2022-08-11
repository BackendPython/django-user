from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import *
from .form import *

class Home(generic.TemplateView):
    template_name = 'index.html'
    
class Registration(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = Easy
    
    def get_success_url(self):
        return reverse('django:login')

class ChangeImg(generic.UpdateView):
    form_class = Img
    template_name = "change-user.html"
    success_url = reverse_lazy("django:home")

    def get_object(self):
        return self.request.user
    
def addfile(request):
    if request.method == "POST":
        form = FileSubmit(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = FileSubmit()

    context = {
        "form": form,
        "file": Admin.objects.all(),
    }
    return render(request, "home.html", context)
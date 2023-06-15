from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomePageView(LoginRequiredMixin, generic.TemplateView):
    template_name = "pages/home.html"

class SignupPageView(generic.TemplateView):
    template_name = "registration/signup.html"
import imp
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

class PaymentView(TemplateView):
    template_name = 'payment.html'
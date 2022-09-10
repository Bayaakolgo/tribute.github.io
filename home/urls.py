from unicodedata import name
from django.urls import path
from .views import HomePageView, PaymentView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
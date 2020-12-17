from django.urls import path
from .import views as pakistan

urlpatterns = [
    path('', pakistan.home, name="homepage"),
    path('about/', pakistan.about, name="aboutus"),
    path('contact/', pakistan.contact, name="contactus"),
]

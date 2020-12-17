from django.shortcuts import render, HttpResponse

# Create your views here.
#home page
def home(request):
    return render(request, 'Home.html')

#about us page
def about(request):
    return render(request, 'About.html')

#contact us page
def contact(request):
    return render(request, 'Contact.html')
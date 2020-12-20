from django.shortcuts import render, HttpResponse

#home page
def home(request):
    return render(request, 'printing/home.html', {})

#about us page
def about(request):
    return render(request, 'About.html', {})

#contact us page
def contact(request):
    return render(request, 'Contact.html', {})
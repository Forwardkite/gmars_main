from django.shortcuts import render

# Create your views here.

def eduhub_home(request):
    return render(request, 'edu_home.html')

def eduhub_about(request):
    return render(request, 'edu_about.html')

def eduhub_service(request):
    return render(request, 'edu_service.html')

def eduhub_contact(request):
    return render(request, 'edu_contact.html')

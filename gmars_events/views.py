from django.shortcuts import render


def events_home(request):
    return render(request, 'events_home.html')

def events_about(request):
    return render(request, 'events_about.html')

def events_cars(request):
    return render(request, 'events_cars.html')

def events_corporate(request):
    return render(request, 'events_corporate.html')

def events_contact(request):
    return render(request, 'events_contact.html')

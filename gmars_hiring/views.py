from django.shortcuts import render
from . models import Job

# Create your views here.

def hiring_home(request):
    jobs = Job.objects.all()
    new_jobs = jobs.order_by('-id')[:5]
    context = {'new_jobs':new_jobs}
    return render(request, 'home.html', context)

def hiring_jobs(request):
    jobs = Job.objects.all()
    context = {'jobs':jobs}
    return render(request, 'jobs.html', context)

def hiring_about(request):
    return render(request, 'about.html')

def hiring_service(request):
    return render(request, 'service.html')

def hiring_contact(request):
    return render(request, 'contact.html')





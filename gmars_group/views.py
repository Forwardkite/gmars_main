from django.shortcuts import render
from . models import Company
# from django.http import HttpResponse

# Create your views here.

def index(request):
    company = Company.objects.all()
    context = {'companies':company}
    return render(request, 'index.html', context)



from django.shortcuts import render
from . models import PopularTour, TopPackage, DomesticPackage, InternationalPackage, MedicalPackage, HotelBooking, TicketBooking

# Create your views here.


def holidays_home(request):
    PopularTours = PopularTour.objects.all()
    TopPackages = TopPackage.objects.all()
    context = {'populartours':PopularTours, 'toppackages':TopPackages}
    return render(request, 'holidays_home.html', context)

def holidays_about(request):
    return render(request, 'holidays_about.html')

def holidays_booking(request):
    HotelBookings = HotelBooking.objects.all()
    TicketBookings = TicketBooking.objects.all()
    context = {'HotelBookings': HotelBookings, 'TicketBookings': TicketBookings}
    return render(request, 'holidays_booking.html', context)

def holidays_tour(request):
    DomesticPackages = DomesticPackage.objects.all()
    InternationalPackages = InternationalPackage.objects.all()
    MedicalPackages = MedicalPackage.objects.all()
    context = {'DomesticPackages': DomesticPackages, 'InternationalPackages':InternationalPackages, 'MedicalPackages': MedicalPackages}
    return render(request, 'holidays_tour.html', context)

def holidays_umrah(request):
    return render(request, 'holidays_umrah.html')

def holidays_visa(request):
    return render(request, 'holidays_visa.html')

def holidays_contact(request):
    return render(request, 'holidays_contact.html')

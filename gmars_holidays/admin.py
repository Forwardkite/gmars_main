from django.contrib import admin
from . models import PopularTour, TopPackage, DomesticPackage, InternationalPackage, MedicalPackage, HotelBooking, TicketBooking

# Register your models here.

admin.site.register(PopularTour)
admin.site.register(TopPackage)
admin.site.register(DomesticPackage)
admin.site.register(InternationalPackage)
admin.site.register(MedicalPackage)
admin.site.register(HotelBooking)
admin.site.register(TicketBooking)



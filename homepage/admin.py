from django.contrib import admin
from .models import UserData, DriverData , Admin , CarCompany ,CarUser, Lift , Booking ,DriverBooking , LiftBooking , Ratings , DriverBlock , UserBlock ,CarBlock , Feedback 
# Register your models here.
admin.site.register(UserData),
admin.site.register(DriverData),
admin.site.register(Admin),
admin.site.register(CarCompany),
admin.site.register(CarUser),
admin.site.register(Lift),
admin.site.register(Booking),
admin.site.register(DriverBooking),
admin.site.register(LiftBooking),
admin.site.register(Ratings),
admin.site.register(DriverBlock),
admin.site.register(UserBlock),
admin.site.register(CarBlock),
admin.site.register(Feedback),





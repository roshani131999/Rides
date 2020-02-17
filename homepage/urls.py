from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contactus',views.contactus,name='contactus'),
    path('feedback',views.feedback,name='feedback'),
    path('userregistration',views.userregistration,name='userregistration'),
    path('ureg',views.ureg,name='ureg'),
    path('driverregistration',views.driverregistration,name='driverregistration'),
    path('dreg',views.dreg,name='dreg'),
    path('login',views.login,name='login'),
    path('authlogin',views.authlogin,name='authlogin'),
    path('userprofile', views.userprofile, name='userprofile'),
    path('updateprofile', views.updateprofile, name='updateprofile'),
    path('rentcar', views.rentcar, name='rentcar'),
    path('rentcaroutput', views.rentcaroutput, name='rentcaroutput'),
    path('useraboutus', views.useraboutus, name='useraboutus'),
    path('userdriveraboutus', views.userdriveraboutus, name='userdriveraboutus'),
    path('driveraboutus', views.driveraboutus, name='driveraboutus'),
    path('bookcar', views.bookcar, name='bookcar'),
    path('driverhome', views.driverhome, name='driverhome'),
    path('userdriverhome', views.userdriverhome, name='userdriverhome'),
    path('bookdriver', views.bookdriver, name='bookdriver'),
    path('driverbooking', views.driverbooking, name='driverbooking'),
    path('driverbook', views.driverbook, name='driverbook'),
    path('driverrequests', views.driverrequests, name='driverrequests'),
    path('driveraccepts', views.driveraccepts, name='driveraccepts'),
    path('driverrejects', views.driverrejects, name='driverrejects'),
    
    path('logout',views.logout,name='logout'),
    
    

]
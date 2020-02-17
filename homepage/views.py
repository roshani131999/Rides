from django.shortcuts import render,redirect
from django.contrib import messages
from .models import UserData,DriverData,CarCompany,CarUser,DriverBooking
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.db.models.expressions import RawSQL
from django.db.models import Case,CharField,Value,When



def index(request):
    return render(request,"index.html")

def home(request):
    return render(request,'home.html',{'app_name':'Smart Rides','tab_name':'Home'})

def aboutus(request):
    return render(request,'aboutus.html',{'app_name':'Smart Ride','tab_name':'About Us'})
def contactus(request):
    return render(request,'contactus.html',{'app_name':'Smart Ride','tab_name':'Contact Us'})
def feedback(request):
    return render(request,'feedback.html',{'app_name':'Smart Ride','tab_name':'Feedback'})


def userregistration(request):
    return render(request,"userregistration.html")

def ureg(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        address = request.POST['address']
        city = request.POST['city']
        gender = request.POST['gender']
        if gender == 'Male':
            ugen = gender
        elif gender == 'Female':
            ugen = gender
        dob = request.POST['dob']
        mobileno = request.POST['mobileno']
        emailid = request.POST['emailid']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        driverregister = request.POST['driverregister']
        if driverregister == 'Yes':
            u = UserData(UFname=firstname, ULname=lastname, Uaddress=address, Ucity=city, Ugender=ugen,
                                    Udob=dob, Umobileno=mobileno, Uemailid=emailid, Upassword=password1)
            u.save()
            return render(request, 'driverregistration.html',{'app_name': 'Smart Ride', 'tab_name': 'Driver Registration', 'firstname': firstname,
                            'lastname': lastname, 'address': address, 'city': city, 'ugen': ugen, 'dob': dob,
                            'mobileno': mobileno, 'emailid': emailid})
        elif driverregister == 'No':
            if password1 == password2:
                u= UserData.objects.all().filter(Uemailid=emailid).count()
                if u!=0:
                    # return HttpResponse(b)
                    return render(request, 'userregistration.html',{'app_name': 'Smart Ride', 'tab_name': 'User Registration', 'firstname': firstname,
                                        'lastname': lastname, 'address': address, 'city': city, 'ugen': ugen, 'dob': dob,
                                        'mobileno': mobileno,'error':'Email taken'})
                else:
                    u = UserData(UFname=firstname, ULname=lastname, Uaddress=address, Ucity=city, Ugender=ugen,
                                    Udob=dob, Umobileno=mobileno, Uemailid=emailid, Upassword=password1)
                    u.save()
                    # messages.info(request, "User Created Successfully")
                    return redirect('login')
            else:
                messages.info(request, "Password not Matching.")
                return redirect('userregistration', {'app_name': 'Smart Ride', 'tab_name': 'User Registration'})
        else:
            pass
    else:
        return render(request, 'userregistration.html', {'app_name': 'Smart Ride', 'tab_name': 'User Registration'})
def driverregistration(request):
    return render(request,'driverregistration.html',{'app_name':'Smart Ride','tab_name':'Driver Registration'})
def dreg(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        address = request.POST['address']
        city = request.POST['city']
        gender = request.POST['gender']
        if gender == 'Male':
            ugen = gender
        elif gender == 'Female':
            ugen = gender
        dob = request.POST['dob']
        mobileno = request.POST['mobileno']
        emailid = request.POST['emailid']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        aadhar = request.POST['aadharno']
        license = request.POST['license']
        insurance = request.POST['insurance']
        bankname = request.POST['bankname']
        bankaccountno = request.POST['bankaccountno']
        ifsc = request.POST['ifsc']
        if password1 == password2:
            b = DriverData.objects.all().filter(Demailid=emailid).count()
            if b!=0:
                return render(request,'driverregistration.html',{'firstname':firstname,'lastname':lastname,'address':address,
                'city':city,'ugen':ugen,'dob':dob,'mobileno':mobileno,'aadhar':aadhar,'license':license,'insurance':insurance,
                'bankaccountno':bankaccountno,'ifsc':ifsc,'app_name':'Smart Ride','tab_name':'Driver Registration','error':'Email taken'})
            else:
                d = DriverData(DFname=firstname,DLname=lastname,Daddress=address,Dcity=city,Dgender=ugen,
                Ddob=dob,DmobileNo=mobileno,Demailid=emailid,Dpassword=password1,Daadhar=aadhar,Dlicenseno=license,
                Dinsurancepolicy=insurance,Dbankname=bankname,Dbankaccountno=bankaccountno,Difsccode=ifsc)
                d.save()
                messages.info(request,"Driver Created Successfully")
                return redirect('login')
        else:
            messages.info(request,"Password not Matching.")
            return redirect('driverregistration',{'app_name':'Smart Ride','tab_name':'Driver Registration'})
    else:
        return render(request,'driverregistration.html',{'app_name':'Smart Ride','tab_name':'Driver Registration'})
def login(request):
    return render(request,'login.html',{'app_name':'Smart Ride','tab_name':'Login'})
def authlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user=UserData.objects.all().filter(UFname=username).filter(Upassword=password)
        driver=DriverData.objects.all().filter(DFname=username).filter(Dpassword=password)
        u=user.count()
        d=driver.count()
        
        # request.session['sessionUFname']=username
        # request.session['sessionUid']=user[0].Uid

        
        if d==1 and u==0:
            request.session['sessionDid']=driver[0].Did
            return render(request,"driverhome.html",{'ufname':username})
        elif u==1 and d==1:
            request.session['sessionUid']=user[0].Uid
            return render(request,"userdriverhome.html",{'ufname':username})
        elif u==1 and d==0:
            request.session['sessionUid']=user[0].Uid
            return render(request,"userhome.html",{'app_name':'Smart Ride','tab_name':'Welcome','ufname':username})

    else:

        return render(request,'login.html',{'app_name':'Smart Ride','tab_name':'Login','error_login':"email or password is wrong..."})

def logout(request):
    return redirect("/")

def userprofile(request):
    uid=request.session['sessionUid']
    data=UserData.objects.all().filter(Uid=uid)
    email1=data[0].Uemailid
    uname=data[0].UFname
    phnno=data[0].Umobileno
    pwd=data[0].Upassword
    return render(request,'myprofile.html',{'ufname':uname,'emailid':email1,'mobileno':phnno,'pwd':pwd})

def updateprofile(request):
    if request.method == 'POST':
        username=request.POST['Username']
        email=request.POST['email']
        phoneno=request.POST['phnno']
        password=request.POST['pwd']

        uid=request.session['sessionUid']
        data=UserData.objects.get(Uid=uid)
        data.UFname=username
        data.Uemailid=email
        data.Umobileno=phoneno
        data.Upassword=password
        data.save()
        return render(request,'myprofile.html')
    else:
        return render(request,'myprofile.html')


def rentcar(request):
    uid=request.session['sessionUid']
    data=UserData.objects.all().filter(Uid=uid)
    uname=data[0].UFname
    return render(request,'rentcar.html',{'ufname':uname})

def rentcaroutput(request):
    if request.method == 'POST':
        carname = request.POST['carname']
        carac = request.POST['carac']
        carimage=request.POST['imgcar']
        notes=request.POST['notes']

        uid=request.session['sessionUid']
        data=UserData.objects.all().filter(Uid=uid)
        isdriver=data[0].Uisdriver
        userid=UserData.objects.get(Uid=uid)

        # carcompany=CarCompany.objects.get(CCID)
        # request.session['sessionccid']=CCID
        # ccid=request.session['sessionccid']
        # ccname=ccid[0].CCname
        caruser=CarUser(CCID=carname,Uid=userid,CUisac=carac,CUnotes=notes,CarImage=carimage,CUIsdriver=isdriver)
        caruser.save()
        return render(request,'userhome.html')
    else:
        return render(request,'rentcar.html')

def useraboutus(request):
    return render(request,'useraboutus.html',{'tab_name':'About Us'})

def userdriveraboutus(request):
    return render(request,'userdriveraboutus.html',{'tab_name':'About Us'})

def driveraboutus(request):
    return render(request,'driveraboutus.html',{'tab_name':'About Us'})

def bookcar(request):
    uid=request.session['sessionUid']
    data=CarUser.objects.all().filter(Uid=uid)
    city=data[0].Ucity
    print(city)
    userdetail=UserData.objects.all().filter(Ucity=city)

    return render(request,'carbooking.html',{'userdetail':userdetail})


def bookdriver(request):
    uid=request.session['sessionUid']
    data=UserData.objects.all().filter(Uid=uid)
    uname=data[0].UFname
    ucity=data[0].Ucity
    drivers=DriverData.objects.all().filter(Dcity=ucity)
    
    # status=request.session['status']

    return render(request,'bookdriver.html',{'app_name':'Smart Ride','tab_name':'Welcome','ufname':uname,'drivers':drivers})

def driverbooking(request):
    if request.method=='GET':
        driverid=request.GET.get('did')
        request.session['sessionDBid']=driverid[0]
    
    # status="pending"
    # request.session['status']=status
    
    # print(status)
    uid=request.session['sessionUid']
    data=UserData.objects.all().filter(Uid=uid)
    uname=data[0].UFname
    ucity=data[0].Ucity
    drivers=DriverData.objects.all().filter(Dcity=ucity)
    return render(request,'driverbooking.html',{'app_name':'Smart Ride','tab_name':'Welcome','ufname':uname,'drivers':drivers})

def driverbook(request):
    uid=request.session['sessionUid']
    data=UserData.objects.all().filter(Uid=uid)
    uname=data[0].UFname
    userid=UserData.objects.get(Uid=uid)
    did=request.session['sessionDBid']
    driverid=DriverData.objects.get(Did=did)

    if request.method=="POST":
        from1 = request.POST['from1']
        to=request.POST['to']
        date=request.POST['date']
        rdate=request.POST['rdate']
        time=request.POST['time']
        dbcancel="1000-01-10"
        db= DriverBooking(Uid=userid,Did=driverid,DBdateofregister=date,DBdate=date,DBTime=time,DBreturndate=rdate,DBDateofcancel=dbcancel,
        DBFrom=from1,DBTo=to)
        db.save()
    
        return render(request,'userhome.html',{'app_name':'Smart Ride','tab_name':'Welcome','ufname':uname})

    else:
        return render(request,'driverbooking.html',{'app_name':'Smart Ride','tab_name':'Welcome','ufname':uname})
    
# this is driver dashboard     
def driverhome(request):
    did=request.session['sessionDid']
    data=DriverData.objects.all().filter(Did=did)
    uname=data[0].DFname
    return render(request,'driverhome.html',{'ufname':uname})

# this view shows the request for a particular driver 
def driverrequests(request):
    did=request.session['sessionDid']
    data=DriverData.objects.all().filter(Did=did)
    uname=data[0].DFname
    data1=DriverBooking.objects.all().filter(Did=did)
    print(data1)
    request.session['sessionDriverBookingid']=data1[0].DBID
    return render(request,'driverrequests.html',{'ufname':uname,'data1':data1})

# this view is called when any driver accepts a request of a user 
def driveraccepts(request):
    did=request.session['sessionDid']
    data=DriverData.objects.all().filter(Did=did)
    uname=data[0].DFname
    # for updating the field "isconfirm" of driver booking table
    DBid=request.session['sessionDriverBookingid']
    DBid1= DriverBooking.objects.get(DBID=DBid)
    DBid1.DBisconform="yes"
    DBid1.save()
    return render(request,'driverhome.html')
# this view is called when any driver rejects the request a user
def driverrejects(request):
    did=request.session['sessionDid']
    data=DriverData.objects.all().filter(Did=did)
    uname=data[0].DFname
    data1=DriverBooking.objects.all().filter(Did=did)
    DBid=request.session['sessionDriverBookingid']
    data2=DriverBooking.objects.get(DBID=DBid)
    # the below code gives the userid from the driverbooking table 
    userid=data2.Uid
    # the below code let you access the data of the userid by comparing the above userid with the UserData table 
    useraccess=UserData.objects.all().filter(Uemailid=userid)
    uid=request.session['sessionUid']
    data=UserData.objects.all().filter(Uid=uid)
    return render(request,'driverhome.html')
    



def userdriverhome(request):
    uid=request.session['sessionUid']
    data=UserData.objects.all().filter(Uid=uid)
    uname=data[0].UFname
    return render(request,'userdriverhome.html',{'ufname':uname})



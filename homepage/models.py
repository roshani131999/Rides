from __future__ import unicode_literals
from django.db import models


# Create your models here.

class DriverData(models.Model):
    Did = models.AutoField(primary_key=True)
    DFname = models.CharField(max_length=50)
    DLname = models.CharField(max_length=50)
    Dpassword = models.CharField(max_length=8)
    Daddress = models.CharField(max_length=50)
    Dcity = models.CharField(max_length=50)
    Ddob= models.DateField(max_length=50)
    Dgender = models.CharField(max_length=50)
    Demailid = models.EmailField(max_length=50)
    DmobileNo = models.CharField(max_length=10)
    Ddoa = models.DateField(auto_now_add=True,blank=True)
    Ddor = models.DateField(auto_now_add=True,blank=True)
    Dlicenseno = models.CharField(max_length=13)
    Dlikecount = models.CharField(default=0,max_length=20)
    Dviewcount = models.CharField(default=0,max_length=20)
    Daadhar = models.CharField(max_length=12)
    Dinsurancepolicy = models.CharField(max_length=10)
    Dbankname = models.CharField(max_length=10)
    Dbankaccountno = models.CharField(max_length=11)
    Difsccode = models.CharField(max_length=11)
    Isauthenticate = models.CharField(default="",max_length=10)


    def __str__(self):
        return self.Demailid


class UserData(models.Model):
    Uid = models.AutoField(primary_key=True)
    UFname = models.CharField(max_length=50)
    ULname = models.CharField(max_length=50)
    Upassword = models.CharField(max_length=8)
    Uaddress = models.CharField(max_length=50)
    Ucity = models.CharField(max_length=50)
    Udob = models.DateField(auto_now_add=True,blank=True)
    Ugender = models.CharField(max_length=50)
    Uemailid = models.EmailField(max_length=50)
    Umobileno = models.CharField(max_length=10)
    Udoa = models.DateField(auto_now_add=True,blank=True)
    Udoj = models.DateField(auto_now_add=True,blank=True)
    Uisauthenticate = models.CharField(max_length=10)
    Uaadhar = models.CharField(max_length=12)
    Ubankname=models.CharField(max_length=12)
    Ubankaccountno = models.CharField(max_length=11)
    Uifsccode = models.CharField(max_length=11)
    Uisdriver = models.CharField(default="no",max_length=10)
    Ulikecount = models.IntegerField(default=0)
    Uviewcount = models.IntegerField(default=0)
    Ulicenseno=models.IntegerField(default=0)
    Uinsurancepolicy=models.CharField(default="",max_length=50)

    def __str__(self):
        return self.Uemailid



class Admin(models.Model):
    AID = models.AutoField(primary_key=True)
    Ausername = models.CharField(max_length=50)
    AFname = models.CharField(max_length=50)
    ALname = models.CharField(max_length=50)
    Apassword = models.CharField(max_length=8)
    Aaddress = models.CharField(max_length=50)
    Acity = models.CharField(max_length=50)
    ADOB = models.DateField(max_length=50)
    Agender = models.CharField(max_length=50)
    Aemail = models.EmailField(max_length=50)
    AmobileNo = models.CharField(max_length=10)
    ADOJ = models.DateField(max_length=50)

    def __str__(self):
        return str(self.AID) + ' - ' + self.Ausername


class CarCompany(models.Model):
    CCID = models.AutoField(primary_key=True)
    CCname = models.CharField(max_length=50)
    Ccapacity = models.CharField(max_length=5)
    Cnotes = models.CharField(max_length=50)

    def __str__(self):
        return str(self.CCID) + ' - ' + self.CCname


class CarUser(models.Model):
    CUID = models.AutoField(primary_key=True)
    Uid= models.ForeignKey(UserData,on_delete=models.CASCADE)
    CCID = models.ForeignKey(CarCompany, on_delete=models.CASCADE)
    CUisac = models.CharField(max_length=50)
    CUminfair = models.CharField(max_length=10,default=50)
    CUacfair = models.CharField(max_length=10,default=50)
    CUnotes = models.CharField(max_length=50)
    CUIsdriver = models.CharField(max_length=50)
    CarImage=models.CharField(max_length=20)

    def __str__(self):
        return str(self.CUID) + ' - ' + self.CUIsdriver

class Lift(models.Model):
    LID = models.AutoField(primary_key=True)
    Uid = models.ForeignKey(UserData, on_delete=models.CASCADE)
    CCID = models.ForeignKey(CarCompany, on_delete=models.CASCADE)
    Ldate = models.DateField(max_length=50)
    LTime = models.TimeField(max_length=50)
    LFplace = models.CharField(max_length=50)
    LTplace = models.CharField(max_length=8)
    Lgender = models.CharField(max_length=50)
    LCharge = models.CharField(max_length=10)
    LIsAc = models.CharField(max_length=50)
    Lcapacity = models.IntegerField()
    Ldateofreturn = models.DateField(max_length=10)
    LIsdone = models.CharField(max_length=50)

    def __str__(self):
        return str(self.LID) + ' - ' + self.LFplace + ' To ' + self.LTplace

class Booking(models.Model):
    BID = models.AutoField(primary_key=True)
    Uid = models.ForeignKey(UserData, on_delete=models.CASCADE)
    CUID = models.ForeignKey(CarUser, on_delete=models.CASCADE)
    Bdate = models.DateField(max_length=50)
    BTime = models.TimeField(max_length=50)
    BFplace = models.CharField(max_length=50)
    BTplace = models.CharField(max_length=8)
    Bdescription = models.CharField(max_length=50)
    Baddress= models.CharField(max_length=10)
    BContactNo = models.CharField(max_length=10)
    BContactname = models.CharField(max_length=50)
    BIsAc = models.CharField(max_length=50)
    Bisconform = models.CharField(max_length=5)
    Bmessage = models.CharField(max_length=10)
    BIscancel= models.CharField(max_length=5)
    BDateofcancel = models.DateField(max_length=50)
    Breasonforcancel = models.CharField(max_length=50)
    BDOR = models.DateField(max_length=50)

    def __str__(self):
        return str(self.BID) + ' - ' + self.BFplace + ' To ' + self.BTplace

class DriverBooking(models.Model):
    DBID = models.AutoField(primary_key=True)
    Uid = models.ForeignKey(UserData, on_delete=models.CASCADE)
    Did=models.ForeignKey(DriverData,on_delete=models.CASCADE)
    DBdateofregister =  models.DateField(max_length=50)
    DBdate = models.DateField(max_length=50)
    DBTime = models.TimeField(max_length=50)
    DBreturndate= models.DateField(max_length=10)
    DBnotes = models.CharField(max_length=50,default="")
    DBisdelete= models.CharField(max_length=10,default="no")
    DBisconform = models.CharField(max_length=5,default="no")
    DBmessage = models.CharField(max_length=50,default="")
    DBIscancel= models.CharField(max_length=5,default="no")
    DBDateofcancel = models.DateField(max_length=50)
    DBreasonforcancel = models.CharField(max_length=50,default="")
    DBFrom=models.CharField(max_length=50)
    DBTo=models.CharField(max_length=50)

    def __str__(self):
        return str(self.DBID) + ' - ' + self.DBisconform

class LiftBooking(models.Model):
    LBID = models.AutoField(primary_key=True)
    LID = models.ForeignKey(Lift,on_delete=models.CASCADE)
    Uid = models.ForeignKey(UserData, on_delete=models.CASCADE)
    LBdate = models.DateField(max_length=50)
    LBTime = models.TimeField(max_length=50)
    LBIsapproved= models.CharField(max_length=10)
    LBmessage = models.CharField(max_length=50)
    LBcapacity= models.CharField(max_length=10)
    LBFplace = models.CharField(max_length=50)
    LBTplace = models.CharField(max_length=50)
    LBIscancel= models.CharField(max_length=5)
    LBDateofcancel = models.DateField(max_length=50)
    LBreasonforcancel = models.CharField(max_length=50)

    def __str__(self):
        return str(self.LBID) + ' - ' + self.LBIsapproved

class Ratings(models.Model):
    RID = models.AutoField(primary_key=True)
    CUID = models.ForeignKey(CarUser,on_delete=models.CASCADE)
    Did = models.ForeignKey(DriverData,on_delete=models.CASCADE)
    Uid = models.ForeignKey(UserData, on_delete=models.CASCADE)
    Rdateofcomment = models.DateField(max_length=5)
    Rdateoflike = models.DateField(max_length=20)
    Rislike= models.CharField(max_length=10)
    Rcomment = models.CharField(max_length=50)

    def __str__(self):
        return str(self.RID) + ' - ' + self.Rislike

class CarBlock(models.Model):
    CBID = models.AutoField(primary_key=True)
    CUID = models.ForeignKey(CarUser,on_delete=models.CASCADE)
    Uid = models.ForeignKey(UserData, on_delete=models.CASCADE)
    CBdateofblock = models.DateField(max_length=20)
    CBnotes = models.CharField(max_length=50)

    def __str__(self):
        return str(self.CBID) + ' - ' + self.CBnotes

class UserBlock(models.Model):
    UBID = models.AutoField(primary_key=True)
    Did = models.ForeignKey(DriverData, on_delete=models.CASCADE)
    Uid = models.ForeignKey(UserData, on_delete=models.CASCADE)
    UBdateofblock = models.DateField(max_length=20)
    UBnotes = models.CharField(max_length=50)

    def __str__(self):
        return str(self.UBID) + ' - ' + self.UBnotes


class DriverBlock(models.Model):
    DBlockID = models.AutoField(primary_key=True)
    Did = models.ForeignKey(DriverData, on_delete=models.CASCADE)
    Uid = models.ForeignKey(UserData, on_delete=models.CASCADE)
    DBlockdateofblock = models.DateField(max_length=20)
    DBlocknotes = models.CharField(max_length=50)

    def __str__(self):
        return str(self.DBlockID) + ' - ' + self.DBlocknotes


class Feedback(models.Model):
    FID = models.AutoField(primary_key=True)
    Fname = models.CharField(max_length=50)
    FDOF = models.DateField(max_length=10)
    FMessage = models.CharField(max_length=100)
    Fisread = models.CharField(max_length=5)
    Fcontactno = models.CharField(max_length=20)
    Femail= models.EmailField(max_length=10)

    def __str__(self):
        return str(self.FID) + ' - ' + self.FMessage
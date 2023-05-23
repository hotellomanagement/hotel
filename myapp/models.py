from django.db import models
import datetime
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from .constants import PaymentStatus
# Create your models here.

class contact(models.Model):
    firstname=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=200)
    message=models.TextField()
    class Meta:
        db_table="contact"
class product(models.Model):
    name=models.CharField(max_length=100)
    mrp=models.FloatField()
    sellingprice=models.FloatField()
    description=models.TextField()
    photo=models.ImageField(upload_to='product/')
    class Meta:
        db_table="product"
    def __str__(self):
        return self.name
    

class blog(models.Model):
    title=models.CharField(max_length=200)
    description=HTMLField()
    photo=models.ImageField(upload_to='blog/')
    postby=models.CharField(max_length=50,default="Admin")
    poston=models.DateField(default=datetime.date.today())
    class Meta:
        db_table="blog"
    def __str__(self):
         return self.title
    
class FAQ(models.Model):
    question=models.TextField()
    answer=models.TextField()
    class Meta:
        db_table="FAQ"
    def __str__(self):
        return self.question
    
    
class Room(models.Model):
    ROOMTYPES=(
        ('Deluxe','Deluxe'),
        ('Super','Super'),
    )
    TYPEOFBED=(
        ('Single','Single'),
        ('Double','Double'),
    )
    AVAIL=(
        ('Yes','Yes'),
        ('No','No')
    )
    Roomtitle=models.CharField (default="",max_length=20)
    photo=models.ImageField(upload_to='blog/')
    typeofbed=models.CharField(max_length=50,choices=TYPEOFBED,default="")
    noofbeds=models.CharField( max_length=100,default="")
    Rating=models.CharField(default='',max_length=20)
    Isavailableroom=models.CharField(max_length=20, choices=AVAIL)
    roomtype=models.CharField(max_length=50,choices=ROOMTYPES,default="")
    price=models.CharField(max_length=100,default="")
    facilities=HTMLField(default="")
    phot1=models.ImageField(upload_to='blog/',default="")
    photo2=models.ImageField(upload_to='blog/',default="")
    photo3=models.ImageField(upload_to='blog/',default="")
    class Meta:
        db_table="Room"
    def __str__(self):
        return self.Roomtitle
    
class customer(models.Model): 
    customerid=models.IntegerField()
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    emailid=models.EmailField(max_length=100)
    
    class Meta:
        db_table="customer"
    def __str__(self):
        return self.customerid    

    
class booking(models.Model): 
    bstatus=(
        ('Pending','Pending'),
        ('Confirmed','Confirmed'),
        ('Cancel','Cancel'),
    )
    firstname=models.CharField( max_length=100,default="")
    lastname=models.CharField( max_length=100,default="")
    checkout=models.CharField(max_length=100,default="")
    checkin=models.CharField(max_length=100,default="")
    phonenumber=models.CharField(max_length=20,default="")
    emailid=models.CharField(max_length=100,default="")
    roomtype=models.ForeignKey(Room,on_delete=models.CASCADE,blank=True,null=True)
    noofadults=models.CharField(max_length=10,default="")
    noofchildren=models.CharField(max_length=10,default='')
    userid=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    status=models.CharField(max_length=20,default='Pending',choices=bstatus)
    class Meta:
        db_table="booking"
    def __str__(self):
        return self.firstname  
    
class subscribe(models.Model): 
    emailid=models.CharField(max_length=100,default="")
    class Meta:
        db_table="subscribe"
    def __str__(self):
        return self.emailid   

class Ordernow(models.Model):
    name = CharField(_("Customer Name"), max_length=254, blank=False, null=False)
    amount = models.FloatField(_("Amount"), null=False, blank=False)
    status = CharField(
        _("Payment Status"),
        default=PaymentStatus.PENDING,
        max_length=254,
        blank=False,
        null=False,
    )
    provider_order_id = models.CharField(
        _("Order ID"), max_length=40, null=False, blank=False
    )
    payment_id = models.CharField(
        _("Payment ID"), max_length=36, null=False, blank=False
    )
    signature_id = models.CharField(
        _("Signature ID"), max_length=128, null=False, blank=False
    )
    bookingid=models.ForeignKey(booking,on_delete=models.CASCADE,blank=True,null=True,related_name="bookings")

    def __str__(self):
        return f"{self.id}-{self.name}-{self.status}"

    






    

    



    


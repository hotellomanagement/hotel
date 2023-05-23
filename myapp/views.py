from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from myapp.forms import *
from django.contrib.auth import login 
import razorpay
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

def order_payment(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        orderid=request.POST.get("provider_order_id")
        bookingid=request.POST.get("bookingid")
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        razorpay_order = client.order.create(
            {"amount": float(amount) * 100, "currency": "INR", "payment_capture": "1"}
        )
        order = Ordernow.objects.create(
            name=name, amount=amount, provider_order_id=razorpay_order['id'],bookingid_id=bookingid
        )
        order.save()
        return render(
            request,
            "payment.html",
            {
                "callback_url": "http://127.0.0.1:8000/callback/",
                "razorpay_key": settings.RAZORPAY_KEY_ID,
                "order": order,
            },
        )
    return render(request, "payment.html")


@csrf_exempt
def callback(request):
    
    razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))
    #    return client.utility.verify_payment_signature(response_data)

    if request.method == "POST":
        try:
            payment_id = request.POST.get("razorpay_payment_id", "")
            provider_order_id = request.POST.get("razorpay_order_id", "")
            signature_id = request.POST.get("razorpay_signature", "")
            params_dict={
                'razorpay_order_id':provider_order_id,
                'razorpay_payment_id':payment_id,
                'razorpay_signature':signature_id

            }
            print(params_dict)
            try:
                order = Ordernow.objects.get(provider_order_id=provider_order_id)
            except:
                return HttpResponse("505 not found inner")
            order.payment_id = payment_id
            order.signature_id = signature_id
            order.save()
            
            result=razorpay_client.utility.verify_payment_signature(params_dict)
            
            if result==True:
                amount=int(order.amount)
                
                try:
                   
                    '''res=razorpay_client.payment.capture(payment_id,{
                        "amount" : amount,
                        "currency" : "INR"
                        })
                    print(res)'''
                    order.status=PaymentStatus.SUCCESS
                    order.save()
                    return render(request, "sucess.html")
                except:
                   
                    order.status=PaymentStatus.FAILURE
                    order.save()
                    return render(request, "failure.html")
            else:
                
                order.status=PaymentStatus.FAILURE
                order.save()
                return render(request, "failure.html")
        except:
            return HttpResponse("505 not found here")
        

# Create your views here.

class homeview(TemplateView):
    template_name="homepage.html" 
class aboutview(TemplateView):
    template_name="about.html" 


class serviceview(TemplateView):
    template_name="service.html" 
class bootview(TemplateView):
    template_name="boot.html" 
class tempview(TemplateView):
    template_name="temp.html" 
class renovatview(TemplateView):
    template_name="renovat.html" 
class formview(TemplateView):
    template_name="form.html" 
class hotelmanagementview(TemplateView):
    template_name="hotelmanagement.html" 
class contactview(TemplateView):
    template_name="contact.html" 
def insertcontact(request):
    if request.method=='POST':
        form=contactform(request.POST)
        if form. is_valid():
            form.save()
            return redirect('/hotelmanagement/')
    else:
        form=contactform()
    return render(request,"contact.html",{'form:form'})

def blogview(request):
    blg=blog.objects.all()
    return render(request,"blog.html",{'blg':blg})

def blogdetail(request,id):
    blg=blog.objects.get(id=id)
    return render(request,"blogdetail.html",{'blg':blg})

def faqsview(request):
    f=FAQ.objects.all()
    return render(request,"faq.html",{'f':f}) 

def signupview(request):
    if request.method=='POST':
        form=signupform(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('/blog/')
    else:
        form=signupform()
    return render(request,"registration/signup.html",{'form':form})        
 
class gallaryview(TemplateView):
    template_name="gallary.html" 

class Roomsview(TemplateView):
    template_name="Rooms.html"

 
def Roomview(request):
    R=Room.objects.all()
    return render(request,"Room.html",{'R':R})  

def Roomdetail(request,id):
    R=Room.objects.get(id=id)
    return render(request,"Roomdetail.html",{'R':R})  

def insertcustomer(request):
    if request.method=='post':
        form=customerform(request.post)
        if form.is_valid():
            form.save()
        return redirect('/customer/')
    else:
        form=customerform()
        return render(request,"customer.html",{'form':form})
def customerview(request):
    return render(request,"customer.html")

def insertbooking(request):
    if request.method=='POST':
        form=bookingform(request.POST)
        if form.is_valid():
            ob=form.save()
            id=ob.pk
            return redirect('pay_booking',id=id)
    else:
        form=bookingform()
    return render(request,"booking.html",{'form':form})
def paybooking(request,id):
    b=booking.objects.get(id=id)
    return render(request,"paybooking.html",{'b':b})
def bookingview(request):
    r=Room.objects.all()
    return render(request,"booking.html",{'r':r})

def insertsubcribe(request):
    if request.method=='POST':
        form=subscribeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/hotelmanagement/')
    else:
        form=subscribeform()
    return render(request,"base.html",{'form':form})

def viewbookingsview(request):
    book=booking.objects.filter(userid_id=request.user.id)
    return render(request,"viewbooking.html",{'book':book})
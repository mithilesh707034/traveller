from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from random import randrange
from django.conf import settings
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from traveller.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http.request import HttpHeaders
#Email
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def home(Request):
    data=City.objects.all()
    return render(Request, "index.html",{'data':data})

def home_page(Request):
    city=City.objects.all()
    package=Package.objects.all().order_by('id')[:10]
    return render(Request, "home.html",{'package':package,'city':city})

def package_list(Request,city):
    package=Package.objects.filter(city=(City.objects.get(slug=city)))
    return render(Request, "third.html",{'package':package})

def package_details(Request,name,id):
    data=Package.objects.get(id=id)
    return render(Request, "details.html",{'data':data})


def bookPackage(Request,id):
    msg1=''
    p=Package.objects.get(id=id)
    city=Package.objects.all()
    city3=City.objects.all()
    package=Package.objects.all().order_by('id').reverse()
    data=Package.objects.get(id=id)
    if(Request.method=="POST"):
        c=Package_Enquiry()
        c.name=Request.POST.get('name')
        c.email=Request.POST.get('email')
        c.phone=Request.POST.get('mobile')
        c.address=Request.POST.get('address')
        c.message=Request.POST.get('message')

        c.package_name=p.name
        c.package_price=p.price
        c.package_description=p.description
        c.package_total_day=p.total_day
        c.start_from=p.start_from
        c.end_to=p.end_to
        c.location_image=p.location_image
        c.save()
        msg1="Done"
    return render(Request,'single-package.html',{'data':data,'city':city,'city3':city3,'package':package,'msg1':msg1})



def signup_page(Request):
    msg=""
    uname=User.objects.all()
    if (Request.method == "POST"):
            p=Request.POST.get('password')
            b = Buyer()
            b.name = Request.POST.get("name")
            b.email = Request.POST.get("email")
            b.phone = Request.POST.get("phone")
            b.address = Request.POST.get("address")
            b.password = p
            try:
                u=Buyer.objects.get(username=b.email)
                if(u):
                   pass
            except:
                   user = User(username=b.email, email=b.email,first_name=b.name)
                   if (user):
                       user.set_password(p)
                       user.save()
                       b.save()
                       msg="Done"
                    #    subject ='Your Account Has Been Successfully Created: Team Farepro'
                    #    message ="Dear "+b.name+"\n\n We are delighted to inform you that your Buyer Account has been successfully created with Team Farepro. We extend our heartfelt gratitude for choosing our platform to access our latest range of products.\n\n Your account details are as follows: \n\n Username: "+b.email +"\n Password:"+p+" \n\n With your new account, you can now explore and purchase our latest products, accessing a wide array of offerings. \n\n If you have any questions or require assistance, please don't hesitate to reach out to our customer support team. We are dedicated to providing you with the best service and ensuring a seamless shopping experience. \n\n Thank you for being a part of Team Farepro. We look forward to serving you with utmost satisfaction.\n \n Best regards,\n Team Farepro."
                    #    email_from = settings.EMAIL_HOST_USER
                    #    recipient_list = [b.email,"dushyant@jdtravelsonline.in" ]
                    #    send_mail( subject, message, email_from, recipient_list )
    return render(Request,"signup.html",{'uname':uname,'msg':msg})



def update_profile(Request,id):
    data = Buyer.objects.get(id=id)
    if (Request.method == "POST"):
        data.name = Request.POST.get("name")
        data.phone = Request.POST.get("phone")
        data.address = Request.POST.get("address")
        data.save()
        return redirect('/profile')
            
    return render(Request,"update-profile.html",{'data':data})



def login_page(Request):
    msg=''
    if (Request.method == "POST"):
        email = Request.POST.get("email")
        password = Request.POST.get("password")
        user = authenticate(username=email, password=password)
        if (user is not None):
            login(Request, user)
            if (user.is_superuser):
                return redirect("/admin")
            else:
                return redirect("/profile")
        
        else:
            msg="Invalid Email or Password!!!!"
    return render(Request, "login.html",{'msg':msg})


@login_required(login_url='/login/')
def logout_page(Request):
    logout(Request)
    return redirect("/login")

@login_required(login_url='/login/')
def profile_page(Request):
    user=User.objects.get(username=Request.user.username)
    buyer = Buyer.objects.get(email=user.username)
    orders = Checkout.objects.filter(user=buyer)
    return render(Request,'profile.html',{'user':buyer,'orders':orders})

@login_required(login_url='/login/')
def add_to_cart(Request, id):
    # Request.session.flush()
    cart = Request.session.get('cart', None)
    p = Package.objects.get(id=id)
    if (cart is None):
        cart = {str(p.id): {'pid': p.id, 'price':p.price}}
    else:
             pass
    Request.session['cart'] = cart
    Request.session.set_expiry(60*60*24*30)
    return redirect("/checkout")

@login_required(login_url='/login/')
def checkout(Request):
   
    return render(Request,'checkout.html')




client = razorpay.Client(auth=(RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY))
@login_required(login_url='/login/')
def orderPage(Request):
    if(Request.method=="POST"):
        # Setting values in session
        Request.session['billing_Name'] = Request.POST.get('billing_name')
        Request.session['billing_Phone'] = Request.POST.get('billing_phone')
        Request.session['billing_Address'] = Request.POST.get('billing_address')
        Request.session['billing_PIN'] = Request.POST.get('billing_pin')
        Request.session['billing_City'] = Request.POST.get('billing_city')
        Request.session['billing_State'] = Request.POST.get('billing_state')
    
        Request.session['shipping_Name'] = Request.POST.get('shipping_name')
        Request.session['shipping_Phone'] = Request.POST.get('shipping_phone')
        Request.session['shipping_Address'] = Request.POST.get('shipping_address')
        Request.session['shipping_PIN'] = Request.POST.get('shipping_pin')
        Request.session['shipping_City'] = Request.POST.get('shipping_city')
        Request.session['shipping_State'] = Request.POST.get('shipping_state')
        user = Buyer.objects.get(email=Request.user.username)
        cart = Request.session.get('cart',None)
        if(cart is None):
            return redirect("/cart")
        else:
                
             for value in cart.values():
                   total = int(value['price'])      
             orderAmount = total*100
             orderCurrency = "INR"
             paymentOrder = client.order.create(dict(amount=orderAmount,currency=orderCurrency,payment_capture=1))
             paymentId = paymentOrder['id']
             if(total):
                          return render(Request,"pay.html",{
                   "amount":orderAmount,
                   "api_key":RAZORPAY_API_KEY,
                   "order_id":paymentId,
                   "User":user
               })   
             
                                
    else:
       pass
 


@csrf_exempt
def payment_fail_redirect(Request):
    return redirect('/checkout')

@csrf_exempt
def payment_success_redirect(Request):
    return redirect('/confirm-order-now')
 
@login_required(login_url='/login/')
def confirm_orderPage(Request):

        user = Buyer.objects.get(email=Request.user.username)
        cart = Request.session.get('cart',None)
        if(cart is None):
            return redirect("/cart")
        else:         
            check = Checkout()
            check.user = user
            total = 0
            gst = 0
            for value in cart.values():
                total = total + int(value['price'])
            check.total = total
            check.gst = 0
            check.final=total+gst
            check.package = Package.objects.get(id=value['pid'])
            check.qty = 1

            check.billing_Name = Request.session.get('billing_Name')
            check.billing_Phone = Request.session.get('billing_Phone')
            check.billing_Address = Request.session.get('billing_Address')
            check.billing_PIN = Request.session.get('billing_PIN')
            check.billing_City = Request.session.get('billing_City')
            check.billing_State = Request.session.get('billing_State')
        
            check.shipping_Name = Request.session.get('shipping_Name')
            check.shipping_Phone = Request.session.get('shipping_Phone')
            check.shipping_Address = Request.session.get('shipping_Address')
            check.shipping_PIN = Request.session.get('shipping_PIN')
            check.shipping_City = Request.session.get('shipping_City')
            check.shipping_State = Request.session.get('shipping_State')
            check.save()        
            subject = "New Booking Received from "+user.name
            html_content = render_to_string('mail-message.html', {'data':check})
            text_content = strip_tags(html_content)
            # Create EmailMultiAlternatives object
            email = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [user.email,'mithileshisdeveloper@gmail.com'])
            email.attach_alternative(html_content, "text/html")
            # Attach Aadhar file if provided
            email.send()
            del Request.session['cart']
        return render(Request,'confirmation.html') 



def about(Request):
     
    return render(Request,'about.html')


def search(Request):
    if Request.method=="POST":
        search=Request.POST.get('search')
        city=Request.POST.get('city')
        package=Package.objects.filter(Q(name__icontains=search)|Q(description__icontains=search))

    return render(Request,'third.html',{'package':package})
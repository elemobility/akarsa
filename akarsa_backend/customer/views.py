
# import pkgutil
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse,redirect
from . import forms as customer_forms
from django.contrib import messages
import random
from django.db.models import Q
from . import models as customer_model
from akarsa_backend import settings
from twilio.rest import Client
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def send_sms(to,data):
    account_sid = settings.ACCOUNT_SID
    auth_token = settings.AUTH_TOKEN
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                         body=data,
                         from_='+18596597899',
                         to='+918057905624'
                     )
    print("this works?")
    print(message.sid,message)
    return message.sid

def buy_product(request,pk):
    if request.user.is_authenticated:
         return  redirect("customer_dashboard")
    elif request.method != 'POST':
        print(request.user)
        f=customer_forms.Login()
        return render(request,"login.html",{"form":f})
    else:
        
       
        c=list(customer_model.Customer.objects.filter(Q(phone_number=request.POST["phone_number"])&Q(country_code=request.POST["country_code"])))

       
        if c==[]:
           
            f=customer_forms.Login(request.POST)
            if f.is_valid():    
                c=customer_model.Customer()
                c.country_code=request.POST["country_code"]
                c.phone_number=request.POST["phone_number"]
                c.otp=random.randint(1000,9999)
                c.save()
                p=customer_model.Product.objects.get(pk=pk)
                order=customer_model.Shopping_order(customer=c,product_id=p)
                order.save()
                order_id=order.id
                print("order_id",order.id)

                print("customer not registered",request.user)
                send_sms('+'+request.POST['country_code']+request.POST['phone_number'],str(c.first_name)+' \n your OTP for Mayani \n'+str(c.otp)
        )
                return  redirect(reverse("customer_enter_otp",kwargs={'pk':int(c.id)}))

        else:
            print("customer registered",request.user)
            c[0].country_code=request.POST["country_code"]
            c[0].phone_number=request.POST["phone_number"]
            c[0].otp=random.randint(1000,9999)
            c[0].save()
            c[0].save()
            p=customer_model.Product.objects.get(pk=pk)
            order=customer_model.Shopping_order(customer=c[0],product_id=p)
            order.save()
            order_id=order.id

            send_sms('+'+request.POST['country_code']+request.POST['phone_number'],str(c[0].first_name)+' \n your OTP for Mayani \n'+str(c[0].otp)
    )
            return redirect(reverse("customer_enter_otp",kwargs={'pk':int(c[0].id)}))



        
        
          
def enter_otp(request,pk):
     if request.method == 'GET':
        f=customer_forms.Otp_verify()
        return render(request,"otpverify.html",{"form":f})
     else:
        c=customer_model.Customer.objects.last()
        c1=customer_model.Customer.objects.get(pk=pk)
       
        print(c1.otp)
        otp = request.POST.get('otp')
        
       
        if c1.otp == otp:
                # f=Otp_verify(request.POST)
                # if c1.otp ==request.POST["otp"]:
            login(request, c1)
            c1.otp = random.randint(1000,9999)
            c1.save()
            user = c1.phone_number
            #return redirect(reverse("customer_dashboard",kwargs={'pk':int(c1.id)})) 
            return redirect(reverse("customer_dashboard"))               # else:
                #     return HttpResponse("invalid otp")
        else:
            # if c1.otp ==request.POST["otp"]:
            print('Wrong')
            return HttpResponse('Data Login Not')
def user_logout(request):
    
    logout(request)
    return HttpResponseRedirect("/home/")

"""

    if request.method != 'POST':
        f=customer_forms.Otp_verify()
        return render(request,"otpverify.html",{"form":f})
    else:
        c=customer_model.Customer.objects.last()
        c1=customer_model.Customer.objects.get(pk=pk)
        if c1!=c:
                f=customer_forms.Otp_verify(request.POST)
                if c1.otp ==request.POST["otp"]:
                    return redirect(reverse("choose_payment",kwargs={'pk':int(c1.id)}))
                else:
                    return HttpResponse("invalid otp")
        else:
            if c1.otp ==request.POST["otp"]:
                return redirect(reverse("customer_dashboard",kwargs={'pk':int(c1.id)}))
       
        
        
 """   
             
             
       
           
   


def dashboard(request): 
    try:  
        if request.method != 'POST':
            #c=customer_model.Customer.objects.get(pk=pk)
            user=request.user
            
            o=list(customer_model.Shopping_order.objects.filter(customer=user))
            f=customer_forms.Dashboard(instance=user)
            return render(request,"dashboard.html",{"form":f,"order":o,"user":user})

        else:
            #c=customer_model.Customer.objects.get(pk=pk)
            user=request.user
            f=customer_forms.Dashboard(instance=user,data=request.POST)
            c1=list(customer_model.Customer.objects.filter((Q(country_code=request.POST['country_code'])&Q(phone_number=request.POST['phone_number']))&~Q(pk=user.id)))
            if c1!=[]:
                return HttpResponse("phone no/email is already registered")
            else:
                if f.is_valid():
                        f.save() 
                    # return redirect(reverse("choose_payment",kwargs={'pk':int(c.id)}))
                        return redirect(reverse("choose_payment"))
    except TypeError:
        return redirect('home')
            
        

        
      
             


#will provide all the subcategory
def sub_category(request,pk):
    sc=customer_model.Sub_category.objects.filter(category_id=pk)
    return render(request,"subcategory.html",{"subcategory":sc})

def sub_concern(request,pk):
    sc=customer_model.Sub_concern.objects.filter(concern_id=pk)
    template = "subcategory.html"
    context = {
        "subconcern":sc,
    }
    return render(request,template,context)

    

def sub_ingrediant(request,pk):
    sc=customer_model.Sub_ingrediant.objects.filter(ingrediant_id=pk)
    return render(request,"subcategory.html",{"subingrediant":sc})

def sub_type(request,pk):
    sc=customer_model.Sub_type.objects.filter(type_id=pk)
    return render(request,"subcategory.html",{"subtype":sc})
def sub_brand(request,pk):
    sc=customer_model.Subbrand.objects.filter(brand_id=pk)
    return render(request,"subcategory.html",{"subbrand":sc})
#end




#will provide all the products in a subcategory
def sub_cattegory_product(request,pk):
    p=customer_model.Product.objects.filter(subcategory=pk)
    return render(request,"subcategory.html",{"subcategory_pro":p})
def sub_concern_product(request,pk):
    p=customer_model.Product.objects.filter(subconcern=pk)
    return render(request,"subcategory.html",{"subconcern_pro":p})
def sub_ingrediant_product(request,pk):
    p=customer_model.Product.objects.filter(subingrediant=pk)
    return render(request,"subcategory.html",{"subingrediant_pro":p})
def sub_brand_product(request,pk):
    p=customer_model.Product.objects.filter(sub_brand=pk)
    return render(request,"subcategory.html",{"subbrand_pro":p})
def sub_type_product(request,pk):
    p=customer_model.Product.objects.filter(subtype_id=pk)
    return render(request,"subcategory.html",{"subtype_pro":p})
# end here

def product_desc(request,pk):
    p=customer_model.Product.objects.filter(pk=pk)
    return render(request,"subcategory.html",{"desc":p})


def make_order(request,pk):
    customer=customer_model.Customer.objects.get(pk=request.POST["customer_id"])
    product=customer_model.Product.objects.get(pk=request.POST["product_id"])
#will get all the categories
def category(request):
    cat=customer_model.Category.objects.all()
    return render(request,"category.html",{"cat":cat})
def concern(request):
    con=customer_model.Concern.objects.all()
    return render(request,"category.html",{"con":con})
def ingrediant(request):
    ingre=customer_model.Ingrediant.objects.all()
    return render(request,"category.html",{"ignre":ingre})
def type(request):
    type=customer_model.Type.objects.all()
    return render(request,"category.html",{"type":type})
def brand(request):
    b=customer_model.Brand.objects.all()
    return render(request,"category.html",{"brand":b})
#end

def home(request):
    return render(request,"home.html")
"""         
    def products_in_cart(request,pk):
    pro=customer_model.Product.objects.filter(cart_id=pk)
    total_items=customer_model.Product.objects.filter(cart_id=pk).count()
    print("test",pro)
    return render(request,"subcategory.html",{"items_in":pro,"total_items":total_items})
    def cart(request,pk):
    customer=customer_model.Customer.objects.get(pk=6)
    product=customer_model.Product.objects.get(pk=3)
    product.customer.add(customer.id)

""" 
def payment(request):
    if request.method != 'POST':
        f=customer_forms.Payment()
       
    else:
        f=customer_forms.Payment(request.POST)
        if f.is_valid():
            
            return  redirect(reverse("customer_dashboard"))

    return render(request,"payment.html",{"form":f})
def add_to_cart(request,pk):
    user = request.user
    prod_id=customer_model.Product.objects.filter(pk=pk)
    

    
   
    cart=customer_model.Cart()
    cart.save(customer_id=user,product_id=prod_id)
    return HttpResponse("success")
def choose_payment(request):
    customer=request.user
    
    
    return render(request,"choosepaymentmethod.html")


def order_review(request):
    user= request.user
    o=list(customer_model.Shopping_order.objects.filter(pk=1))
    print("order",o)
  
    
    return render(request,"otpverify.html",{"order":o})


def Shopping_order(request,pk):
    user=request.user
    p=customer_model.Product.objects.get(pk=pk)
    order=customer_model.Shopping_order(customer=user,product_id=p)
    order.save()
   
    return render(request,"orderreview.html",{"p":p})


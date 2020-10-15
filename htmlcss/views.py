from django.shortcuts import render
from .models import Customer
from .models import Restaurant
from .models import Meals

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'aboutus.html')

def cont(request):
    return render(request, 'contact.html')

def custHome(request):
    return render(request, 'CustomerHomepage.html')

def custReg(request):
    return render(request, 'customerRegistration.html')

def custSamp(request):
    return render(request, 'customersamplepage.html')

def restHome(request):
    return render(request, 'RestaurantHomepage.html')

def restInp(request):
    return render(request, 'RestaurantInput.html')

def restReg(request):
    return render(request, 'RestaurantRegistration.html')

def sendMes(request):
    return render(request, 'SendMessage.html')

def wh(request):
    return render(request, 'why.html')

def logI(request):
    return render(request, 'login.html')

def actionC(request):
    fname = request.POST.get("first-name")
    lname = request.POST.get("last-name")
    idd = request.POST.get("id")
    ema = request.POST.get("email")
    pas = request.POST.get("psw")

    o_ref = Customer(firstName=fname, lastName=lname, idNum=idd, email=ema, passWords=pas)
    o_ref.save()

    return render(request, "CustomerHomepage.html")

def actionR(request):
    nam = request.POST.get("business-name")
    ad = request.POST.get("address")
    ei = request.POST.get("id")
    emai = request.POST.get("email")
    passs = request.POST.get("psw")

    h_ref = Restaurant(busName=nam, busAddress=ad, einNum=ei, busEmail=emai, busPassWords=passs)
    h_ref.save()

    return render(request, "RestaurantHomepage.html")

def actionCH(request):
    addr = request.POST.get("location")
    Customer.custAddress = addr

    return render(request, "customersamplepage.html")



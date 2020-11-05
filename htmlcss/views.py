from django.shortcuts import render
from .models import Customer
from .models import Restaurant
from .models import Meals
from .models import LocationArea
from .models import ContactUs
from django.contrib.auth import authenticate, login

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

def actionRH(request):
    addre = request.POST.get("location")
    Restaurant.busAddress = addre

    return render(request, "RestaurantInput.html")

def actionL(request):
    e = request.POST.get("email")
    pj = request.POST.get("psw")

    user = authenticate(request, email=e, passWords=pj)
    if user is None:
        return render(request, "login.html", {"message": "incorrect login!"})

def restSamp(request):
    return render(request, "Restaurantsamplepage.html")

def contactPage(request):
    na = request.POST.get("name")
    em = request.POST.get("email")
    ph = request.POST.get("phone")
    mee = request.POST.get("message")

    u = ContactUs(nameC=na, emailC=em, phoneC=ph, messageC=mee)
    u.save()

    return render(request, "SendMessage.html")

def actionRI(request):
    d = request.POST.get("dish")
    di = request.POST.get("dishnum")
    dis = request.POST.get("dishes")

    lo = Meals(mealType=d, mealAvail=di)
    lo.save()

    return render(request, "Restaurantsamplepage.html")





from django.shortcuts import render, redirect
from .models import Customer, RestaurantMore
from .models import Restaurant
from .models import ContactUs
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib import messages
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth import get_user_model

User = get_user_model()


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

    o_ref = Customer(firstName=fname, lastName=lname, idNum=idd, email=ema, password=pas)
    o_ref.save()

    return render(request, "UploadProfileCust.html")

@login_required
@allowed_users(allowed_roles=['customer'])
def proPage(request):

    return render(request, "sampleUserProfile.html")

def actionR(request):
    nam = request.POST.get("business-name")
    ad = request.POST.get("address")
    ei = request.POST.get("id")
    emai = request.POST.get("email")
    passs = request.POST.get("psw")

    h_ref = Restaurant(name=nam, email=emai, password=passs, idNum=ei)
    h_ref.save()

    return render(request, "HeaderNLogoRest.html")

def actionCH(request):
    addr = request.POST.get("location")
    Customer.custAddress = addr

    return render(request, "customersamplepage.html")

def actionRH(request):
    addre = request.POST.get("location")
    Restaurant.busAddress = addre

    return render(request, "RestaurantInput.html")

def restSamp(request):
    return render(request, "Restaurantsamplepage.html")

def actionL(request):
    e = request.POST.get("email")
    p = request.POST.get("psw")

    return render(request, "login.html")

def custAbout(request):
    return render(request, "CustAbout.html")

def custWhy(request):
    return render(request, "CustWhy.html")

def custCont(request):
    return render(request, "CustContact.html")


def contactPage(request):
    na = request.POST.get("name")
    em = request.POST.get("email")
    ph = request.POST.get("phone")
    mee = request.POST.get("message")

    u = ContactUs(nameC=na, emailC=em, phoneC=ph, messageC=mee)
    u.save()

    return render(request, "SendMessage.html")

def pastRec(request):
    return render(request, "PastReceipt.html")

def actionRI(request):
    d = request.POST.get("dish")
    di = request.POST.get("dishnum")
    dis = request.POST.get("dishes")


    return render(request, "AddRemoveMenu.html")

def head(request):
    p = request.POST.get("restLogo")
    l = Restaurant.profile_pic(p)
    l.save()
    return render(request, "RestaurantHomepage.html")

def regRec(request):
    return render(request, "receiptSample.html")

@unauthenticated_user
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created! You are now able to log in!')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
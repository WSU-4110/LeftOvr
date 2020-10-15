from django.shortcuts import render

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




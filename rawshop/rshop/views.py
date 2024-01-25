from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def cart(request):
    shoeslist={'b1':'Adidas','b2':'Nike'}
    return render(request,'cart.html',shoeslist)

def payment(request):
    return render(request,'payment.html')

def profile(request):
    return render(request,'profile.html')
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'shop/index.html')

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return render(request,'shop/contact.html')

def search(request):
    return render(request,'shop/search.html')

def tracker(request):
    return render(request,'shop/tracker.html')

def productVeiw(request):
    return render(request,'shop/productveiw.html')

def checkout(request):
    return render(request,'shop/checkout.html')
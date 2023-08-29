from django.shortcuts import render

# Create your views here.
def index (request):
    
    return render(request,'index.html')


def positional(request):
    
    return render(request,'positional.html')

def home(request):
    
    return render(request,'home.html')

def catering(request):
    
    return render(request,'catering.html')



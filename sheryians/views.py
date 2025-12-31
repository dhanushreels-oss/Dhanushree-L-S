from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def course(request):
    return render(request,'course.html')

def request(request):
    return render(request,'request.html')

def signin(request):
    return render(request,'signin.html')

def  register (request):
    return render(request, 'register.html')
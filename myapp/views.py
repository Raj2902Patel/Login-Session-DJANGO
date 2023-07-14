from django.shortcuts import render,redirect
from .models import registerdata
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def index(request):
    if 'email' in request.session:
        regidata = request.session['email']
        mail = {'regidata':regidata}
        return render(request,'index.html',mail)
    
    else:
        return redirect('login')
    
    return render(request,'login.html')

def fetchregisterdata(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            validateuser = registerdata().objects.get(email=email)
        except:
            validateuser = None

        if validateuser is None:
            query = registerdata(name=name,email=email,password=password)
            query.save()
        else:
            messages.error(request,'You are Already Registered. Please Login')
            return render(request,'login.html')
    else:
        pass
    return render(request,'register.html')

def fetchlogindata(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        checkuser = registerdata.objects.filter(email=email,password=password)
        if checkuser:
            request.session['email'] = email
            return redirect('index')
        else:
            return HttpResponse('Please Enter Valid Email Id')
    return render(request,'login.html')

def logout(request):
    try:
        del request.session['email']
    except:
        return redirect('login')
    
    return redirect('login')
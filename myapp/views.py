from django.shortcuts import render,redirect
from .models import registerdata
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password

print(make_password('1234'))
print(check_password('1234','pbkdf2_sha256$720000$iGek4Cstbd2q6Bv1oPLld0$u8emqyeVunPkRxeskZWZ6MqqMxdFYaUS4ts+ckTEM/o='))

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
            query.password = make_password(query.password)
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

        checkuser = registerdata.objects.get(email=email)

        check = check_password(password,checkuser.password)
        if check:
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
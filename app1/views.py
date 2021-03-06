from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
from app1.form import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def register(request):
    userform=UserForm()
    profileform=ProfileForm()
    if request.method=='POST' and request.FILES:
        UD=UserForm(request.POST)
        PD=ProfileForm(request.POST,request.FILES)
        if UD.is_valid() and PD.is_valid():
            us=UD.save(commit=False)
            pw=UD.cleaned_data['password']
            us.set_password(pw)
            us.save()
            ps=PD.save(commit=False)
            ps.user=us
            ps.save()
            send_mail('Registration',
            'Thanks',
            'nitheshtulluru1998@gmail.com',
            [us.email],fail_silently=False)
            return HttpResponse('Registration is successfull')

            
    d={'userform':userform,'profileform':profileform}
    return render(request,'register.html',d)



    
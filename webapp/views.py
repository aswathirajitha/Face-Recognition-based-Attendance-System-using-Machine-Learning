from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, StudentForm,leaveForm,displayForm

from .models import details, leave, disp

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create your views here.
def about (request):
    return render(request,'one.html')

def home(request):
    return render(request,'home.html')

def sthome(request):
    return render(request,'sthome.html')

def detail(request):
    return render(request,'details.html')

def leaves(request):
    if request.method =='POST':
        lev = leaveForm(request.POST)
        if lev.is_valid():
            lev.save()
            return redirect('sthome')
    else:
        lev =leaveForm()
    return render(request,'leave.html',{'lev':lev})



def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            # messages.success(request,'Account was created for' + user)
            return redirect('login')
    context = {'form':form} 
    return render(request,'register.html',context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password') 
        user= authenticate(request,username=username,password=password)  
        if user is not None:
            auth_login(request,user)
            return redirect('home.html')
        else:
            messages.info(request,'Username OR password is incorrect')
    context = {}
    return render(request,'login.html',context)

def stlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password') 
        user= authenticate(request,username=username,password=password)  
        if user is not None:
            auth_login(request,user)
            return redirect('sthome.html')
        else:          
             messages.info(request,'Username OR password is incorrect')
    context = {}
    return render(request,'stlogin.html',context)


def addstudents(request):
    if request.method =='POST':
        frm = StudentForm(request.POST,request.FILES or None)
        if frm.is_valid():
            frm.save()
            return redirect('home')
    else:
        frm =StudentForm()
    return render(request,'details.html',{'frm':frm})


def simple_function(request):
    os.system("start cmd")
    return render(request,'home.html')


def readfile(request):
    f = open('C:/Users/Aswathi/Desktop/att/webatt/face_rec-code/attend.txt', 'r')
    if f.mode == 'r':
       contents =f.read()
       print (contents)
       X=contents[:9]
       print(X)
       Y=contents[10:19]
       print(Y)
       Z=contents[20:] 
       print(Z)
    #    t=","
    #    Z=t.join(Z)
    #    print(Z)
       context={'X':X,'Y':Y,'Z':Z}
       return render(request,'att.html',{'context':context})
    else:
        return render(request,'home.html')

def attendview(request):
    student_list=details.objects.all()
    return render(request,'attendance.html',{'student_list':student_list})

def delete_item(request,myid):
    item = details.objects.get(id=myid)
    item.delete()
    messages.info(request,'delete successfully')
    return redirect('attendview')



def edit_item(request,myid):
    stud_item = details.objects.get(id= myid)
    stud_list = details.objects.all()
    context = {
        'stud_item':stud_item,
        'stud_list':stud_list
    }
    return render(request,'details.html', context)


def update_item(request,myid):
    item = details.objects.get(id= myid)
    item.name = request.POST['name']
    item.reg_no = request.POST['reg_no']
    item.course = request.POST['course']
    item.batch = request.POST['batch']
    item.image = request.POST['image']
    
    item.save()
    messages.info(request, "item Updated Successfully")
    return redirect('attendview')

def leave_view(request):
    stude_list=leave.objects.all()
    return render(request,'leave_view.html',{'stude_list':stude_list})


def verify(request):
    obj = details.objects.all()
    if request.method=="POST":
        co=request.POST.get('verify')
        if co!=None:
            co_num=details.objects.filter(reg_no=co)
            print(co_num)
            if co_num is not None and co is not None:
                # print(passnum)
                a=co_num.values('reg_no')
                print(a)
                b=details.objects.filter(reg_no=co).values()                    # b=a.values()
                print(b)
                for i in b:
                    print(i)
                    return render(request, 'verify.html',{'i':i})
            else:
                messages.info(request,'Username OR password is incorrect')
            
                

        else:
            pass
    return render(request,'verify.html')   


def display_att(request):
    if request.method =='POST':
        fm = displayForm(request.POST,request.FILES or None)
        if fm.is_valid():
            fm.save()
            return redirect('home')
    else:
        fm =displayForm()
    return render(request,'display.html',{'fm':fm})



# def att(request):
#     obj = disp.objects.all()
#     objs = disp.objects.filter().only('files')
#     print(objs)
    
#     if request.method=="POST":
#         ch=request.POST.get('display')
#         if ch!=None:
#             ch_num=disp.objects.filter(dates=ch)
#             print(ch_num)
#             if ch_num is not None and ch is not None:
#                 # print(passnum)
#                 # c=ch_num.values('dates')
#                 # print(c) 
#                 j=disp.objects.filter(dates=ch).values()
#                 print(j)
#                 for v in j:
#                     print(v)
#                     hh={'v':v,
#                     'objs':objs}
#                     return render(request,'att_view.html',hh)
#     return render(request,'att_view.html')
    #         if ch_num is not None and ch is not None:
    #             # print(passnum)
    #             c=ch_num.values('date')
    #             print(c)
    #             j=disp.objects.filter(date=ch).values()                    # b=a.values()
    #             print(j)
    #             for v in j:
    #                 print(v)
    #                 hh={'v':v}
            # return render(request, 'att_view.html')
    #         else:
    #             pass


def single_view(request):
    obj = disp.objects.all()
    return render(request,'att_view.html',{'obj':obj})

            
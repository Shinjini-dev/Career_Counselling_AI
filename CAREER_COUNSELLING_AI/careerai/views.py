from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .gemini import get_gemini_response 


# Create your views here.
def home(request):
    return render(request,'home.html')
def contact(request):
    return render(request,'contact.html')

def service(request):
    return render(request,'service.html')

# Login Page
def user_login(request):
    if request.method=='POST':
        uname=request.POST['username']
        pwrd=request.POST['password']
        user=authenticate(username=uname,password=pwrd)
        if user:
            login(request,user)
            messages.success(request,"Login Successful!")
            return redirect ('homepage')
        else:
            messages.error(request,"Inavlid username or Password!")
            return render(request,'login.html')
    else:
        return render(request,'login.html')


# Registration Page
def user_register(request):
    if request.method=='POST':
        uname=request.POST['username']
        pword=request.POST['password']
        email=request.POST['email']
        if User.objects.filter(username=uname).exists():
            messages.error(request, "username already exists.")
            return redirect('register')
        user=User.objects.create_user(username=uname,password=pword,email=email)
        user.save()
        # if user(login,request):
        messages.success(request, "Registration Successful! Please login.")
        return redirect ('login')
    return render(request,'register.html')

# LogOut Page
def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('homepage')



# Gemini

def career_chat_ai(request):
    answer= ""
    user_question = ""  
    if request.method == "POST":
        user_question=request.POST.get("question")
        if user_question:
            answer=get_gemini_response(user_question)
        else:
            answer="Please enter a question before submitted"

    return render(request,"career_chat.html",{"answer":answer,"question":user_question})




# 


from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from auth_module.models import *
from .EmailBackEnd import EmailBackEnd

def base(request):
    return render(request,'base.html')

def landing(request):
    return render(request,'index.html')

def register(request):
    return render(request, 'register_user.html')

def login_page(request):
    return render(request,'login.html')


def dologin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password'),)
        if user is not None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('admin_home')

            elif user_type == '2':
                return redirect('view_students')

            elif user_type == '3':
                return redirect('view_group')

            else:
                messages.error(request,'Email and Password are Invalid !')
                return redirect('login_page')
        else:
            messages.error(request, 'Email and Password are Invalid !')
            return redirect('login_page')
        
def check_email(request):
    if request.method == "POST":
        email = request.POST.get('email')
        user = CustomUser.objects.filter(email=email)
        if user.exists():
            context = {
                'email': email
            }
            return render(request, 'reset_password.html', context)
        messages.error(request, f'Sorry, No User Found with this Email!')
        return redirect("login_page")
    else:
        return redirect('login_page')

def reset_password(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = CustomUser.objects.filter(email=email)
        if user.exists():
            user = user.first()
            user.set_password(password)
            user.save()
            messages.success(request, 'Your Password has been successfully updated !')
            return redirect('login_page')
    else:
        return redirect('login_page')

def dologout(request):
    logout(request)
    return redirect('landing')


@login_required(login_url='/')
def profile(request):
    user = CustomUser.objects.get(id = request.user.id)
    print(user)

    context={
        "user":user,
    }
    return render(request,'profile.html',context)

@login_required(login_url='/')
def profile_update(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name=request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(profile_pic,first_name,last_name,email,username,password)
        #print(profile_pic)
        try:
            customuser=CustomUser.objects.get(id = request.user.id)

            customuser.first_name = first_name
            customuser.last_name = last_name

            if password !=None and password != "":
                 customuser.set_password(password)
            if profile_pic !=None and profile_pic != "":
                 customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request, 'Your Profile Updated Successfully !')
            return redirect('profile')
        except:
            messages.error(request,'failed to update your profile !')
    return render(request, 'profile.html')


def add_student(request):

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        programe = request.POST.get('programe')
        academic_year = request.POST.get('academic_year')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')


        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'email is already taken')
            return redirect('add_student')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username is already taken')
            return redirect('add_student')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=3
            )
            user.set_password(password)
            user.save()

            student = Student(
                admin=user,
                programme=programe,
                gender=gender,
                dob = dob,
                phone = phone,
                academic_year = academic_year
            )
            student.save()
            messages.success(request,"Details of" + user.first_name + " " + user.last_name + " are Successfully Saved !" )
            return redirect('landing')

    return render(request,'register_student.html')


def add_cordinator(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        role = request.POST.get('role')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, ' email is already taken')
            return redirect('add_cordinator')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, ' Username is already taken')
            return redirect('add_cordinator')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=2
            )
            user.set_password(password)
            user.save()

            cordinator = Coridinator(
                admin=user,
                phone = phone,
                gender=gender,
                role=role,
                status='Added'
            )
            cordinator.save()
            messages.success(request,"Details of" + user.first_name + " " + user.last_name + " are Successfully Saved !" )
            return redirect('landing')
    return render(request, 'register_cordinator.html')

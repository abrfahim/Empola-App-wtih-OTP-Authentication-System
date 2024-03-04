from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Profile
import random
from django.core.mail import send_mail
from django.conf import settings
#create your views here

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            profile = Profile.objects.get(user=user)
            profile.save()
            if profile.is_verified==True:
                login(request, user)
                messages.success(request,'Log in successful!')
                return redirect('person:all_profile')
            else:
                messages.warning(request, 'You are not verified! Please try to login again')
                return redirect('registration:login_user')
            
        else:
            messages.warning(request, "Invalid username or password!")
            return redirect('registration:login_user')
        
    return render(request, 'registration/login.html')

def register_user(request):
    '''
    User Registration & Authentication Process Using OTP
    '''
    print(register_user.__doc__)
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.warning(request,"User already exists! Try another!")
                return redirect('register_user')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.set_password(password1)
                user.save()
                otp = random.randint(0000, 9999)
                print(otp)
                profile = Profile(user=user,token=otp)
                profile.save()
                
                subject = 'Your Account Verification OTP'
                message = f"Here is your OTP: {otp}"
                from_email = settings.EMAIL_HOST_USER
                recipent = [email]
                
                send_mail(subject, message, from_email, recipent)
                messages.success(request,"Account created to verify check your mail for otp!")
                return redirect('registration:verify_account')
        else:
            messages.warning(request,"Your given password didn't match!")
        
    return render(request, 'registration/register.html')

# def send_mail(email, token):
#     subject = 'Your Account Verification OTP'
#     message = f"Here is your OTP: {token}"
#     from_email = settings.EMAIL_HOST_USER
#     recipent = [email]
    
#     send_mail(subject, message, from_email, recipent)
#     pass


def reset(request):
    return render(request, 'registration/reset.html')


def verify_account(request):
    if request.method == 'POST':
        verify_otp = request.POST.get('verify_otp')
        print(verify_otp)
        
        try:
            profile = Profile.objects.get(token=verify_otp)
            profile.is_verified = True
            profile.save()
            messages.success(request,'Account Verified Successfully done!')
            return redirect('registration:login_user')
        except:
            messages.warning(request,'OTP verification failed!')
            return redirect('registration:verify_account')
            
    return render(request, 'registration/otp.html')


@login_required
def logout_user(request):
    logout(request)
    messages.warning(request, "You have been logged out!")
    return redirect('registration:login_user')

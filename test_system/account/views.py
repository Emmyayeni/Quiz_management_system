from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render,redirect
from django.views import View
from account.form import RegistrationForm
from django.contrib import messages
from account.models import Account,Student,Staff,Employee,Employer
# Create your views here.
import json
from .forms import RegistrationForm


class RegistrationView(View):
    form = RegistrationForm()
    def get(self,request):
        # email 
        #username
        # profile_image
        #bio
        # date of birth 
        return render(request,'account/register.html')

    def post(self,request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            account_type = request.POST.get("account_type")
            if account_type == "student":
                student = Student.objects.create(user=account)
                student.save()
            elif account_type == "lecturer":
                account.is_staff = True
                lecturer = Staff.objects.create(user=account)
                lecturer.save()
                account.save()
            elif account_type =="employee":
                employee = Employee.objects.create(user=account)
            elif account_type =="employer":
                employer = Employer.objects.create(account)
            return redirect('login')
        else:
            messages.error(request,"An error occurred during registration")
        return render(request,'account/register.html')
        
class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('home')
    

def Login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = Account.objects.get(email=email)
        except:
            messages.error(request,'User does not exits')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Username Or password does not exit')
    return render(request,'account/login.html')
    

from django.shortcuts import render
from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render,redirect
from django.views import View
from account.form import RegistrationForm
from django.contrib import messages
from account.models import Account,Student,Staff,Employee,Employer
# Create your views here.
import json


class RegistrationView(View):
    def get(self,request):
        # email 
        #username
        # profile_image
        #bio
        # date of birth 
        return render(request,'account/register.html')

    def post(self,request):
        data = json.loads(request.body)
        print(data)
        return
        
class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('home')
    

class Login(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request,'account/login.html')
    def post(self,request):
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
        return render(request, 'account/login.html')

        
class StudentView(View):
    form_class = RegistrationForm()
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request,'account/register.html',{'form':self.form_class})
    def post(self,request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email,password=raw_password)
            student = Student.objects.create(user=account)
            student.save()
            return redirect('home')
        else:
            messages.error(request, 'something went wrong check your form')
        return render(request,'account/register.html',{'form':form})

class StaffView(View):
    form = RegistrationForm()
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request,'account/register.html',{'form':self.form})
    def post(self,request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email,password=raw_password)
            staff = Staff.objects.create(user=account)
            staff.save()
            return redirect('home')
        else:
            messages.error(request, 'something went wrong check your form')
        return render(request,'account/register.html',{'form':form})
   
class EmployeeView(View):
    form = RegistrationForm()
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request,'account/register.html',{'form':self.form})
    def post(self,request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email,password=raw_password)
            employee = Employee.objects.create(user=account)
            employee.save()
            return redirect('home')
        else:
            messages.error(request, 'something went wrong check your form')
        return render(request,'account/register.html',{'form':form})
   
class EmployerView(View):
    form = RegistrationForm()
    def get(self,request):
        if request.user.is_authenticated:
           return redirect('home')
        return render(request,'account/register.html',{'form':self.form})
    def post(self,request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email,password=raw_password)
            employer = Employer.objects.create(user=account)
            employer.save()
            return redirect('home')
        else:
            messages.error(request, 'something went wrong check your form')
        return render(request,'account/register',{'form':form})

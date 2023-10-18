from django.urls import path
from account.views import RegistrationView,Logout,Login,StudentView,StaffView,EmployeeView,EmployerView


urlpatterns = [
    path('register',RegistrationView.as_view(),name='register'),
    path('register_student',StudentView.as_view(),name='register_student'),
    path('register_lecturer',StaffView.as_view(),name='register_lecturer'),
    path('register_employee',EmployeeView.as_view(),name='register_employee'),
    path('register_employer',EmployerView.as_view(),name='register_employer'),
    path('logout',Logout.as_view(),name='logout'),
    path('login',Login,name='login'),
]

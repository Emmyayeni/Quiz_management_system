from django.urls import path
from account.views import RegistrationView,Logout,Login


urlpatterns = [
    path('register',RegistrationView.as_view(),name='register'),
    path('logout',Logout.as_view(),name='logout'),
    path('login',Login,name='login'),
]

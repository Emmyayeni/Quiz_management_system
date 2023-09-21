from django.contrib import admin
from django.urls import path,include
from .views import questions,create_question,question_create,addTest,exam,register

urlpatterns = [
    path('question',questions,name="question"),
    path('register',register,name="register"),
    path('create_question',create_question, name="create_question"),
    path('question_create',question_create, name="question_create"),
    path('addtest',addTest, name="addtest"),
    path('exam',exam,name='exam')


]
from django.urls import path
from staff.views import home,create_test,student_list,single_page,create_quiz

urlpatterns = [
    path('',home,name="staff_home"),
    path('create_test',create_test,name="create_test"),
    path('students',student_list,name="students"),
    path('single',single_page,name="single"),
    path('create_quiz',create_quiz,name="create_quiz"),

    # path('create_question',)
]

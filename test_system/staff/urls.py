from django.urls import path
from staff.views import staff_home,create_test,student_list,single_page,create_quiz

urlpatterns = [
    path('',staff_home,name="staff_home"),
    path('create_test',create_test,name="create_test"),
    path('students',student_list,name="students"),
    path('question_<q_id>',single_page,name="single"),
    path('create_quiz',create_quiz,name="create_quiz"),

    # path('create_question',)
]

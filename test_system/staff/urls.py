from django.urls import path
from staff.views import staff_home,create_test,student_list,profile_page,single_page,create_quiz,performance,update_question

urlpatterns = [
    path('',staff_home,name="staff_home"),
    path('create_test',create_test,name="create_test"),
    path('students',student_list,name="students"),
    path('question_<q_id>',single_page,name="single"),
    path('create_quiz',create_quiz,name="create_quiz"),
    path('profile',profile_page,name='profile'),
    path('performance',performance,name='performance'),
    path('update_question',update_question,name='update_question'),

    # path('create_question',)
]

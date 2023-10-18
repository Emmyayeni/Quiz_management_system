from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from testapp.models import Questions
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
@staff_member_required
def staff_home(request):
    return render(request,'staff/home.html')

# def view_student(request):
#     return 

def create_test(request):
    user = request.user
    questions = Questions.objects.filter(created_by=user)
    context = {"questions":questions}
    # return test template here
    return render(request,'staff/snippets/create_test.html',context)


def student_list(request):
    return render(request,'staff/snippets/student.html')

def single_page(request,*args,**kwargs):
    q_id = kwargs.get('q_id')
    question = Questions.objects.get(id=q_id)
    answers = question.answer_options
    context={"question":question,"answers":answers}
    return render(request,'staff/snippets/single_page.html',context)

def create_quiz(request):
    return render(request,'staff/snippets/create_quiz.html')
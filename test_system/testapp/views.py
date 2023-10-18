from django.shortcuts import render,redirect
from .models import Questions, AnswerOptions,Course,TotalCourseTest,Student
from testapp.models import Test
import json
from django.http import JsonResponse
import random
from django.core.paginator import Paginator



# Create your views here.

def home(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('staff_home')
        else:
            try:
                Student.objects.get(user=request.user)
            except Student.DoesNotExist:
                pass
            return redirect('student_home')
    return render(request, 'home.html')


def questions(request):
    question = Questions.objects.all()
    context = {"questions": question}
    return render(request, 'testapp/questions.html', context)

def save_question(request):
    datas = json.loads(request.body)
    data = datas['form']
    user = request.user 
    answery = data['answer']
    testt = Questions.objects.get(question=data['question'])
    course = Course.objects.get(name=data['course'])
    try:
        q_test = Test.objects.get(user=user,course=course,question=testt)
    except Test.DoesNotExist:
        q_test = Test.objects.create(user=user,course=course,question=testt)
    q_test.answer = data['answer']
    q_test.score = q_test.calculate_test_score()
    q_test.save()
    return JsonResponse('Successfully added answer')

def submit_question(request):
    datas = json.loads(request.body)
    data = datas['form'] 
    coursey = data['course']

    user = request.user
    course = Course.objects.get(name=coursey)
    quiz = TotalCourseTest.objects.create(user=user,course=course)
    quiz.add_questions()
    quiz.total_score = quiz.calculate_total_score()
    quiz.save()
    return JsonResponse("successfully submited questions")
    

def create_question(request):
    data = json.loads(request.body)
    datas = data['form']
    print(datas['question'])
    question = datas['question']
    user = request.user
    answer = AnswerOptions.objects.create(a=datas['a'], b=datas['b'], c=datas['c'], d=datas['d'])
    questions = Questions.objects.create(question=question, answer_options = answer,correct_answer=datas['correct_answer'], created_by=user)
    answer.save()
    questions.save()
    return JsonResponse('payment complete', safe=False)

def question_create(request):
    questions = Questions.objects.all()
    new_list = random.sample(list(questions),3)
    print(new_list)
    
    return render(request, 'testapp/create_questions.html')


def addTest(request):
    datas = json.loads(request.body)
    fomm = datas['form']
    print(datas)
    return JsonResponse(f'test added {datas}', safe=False)


def exam(request):
    exam_list = Questions.objects.all()
    paginator = Paginator(exam_list,1)
    page = request.GET.get('page')
    list = paginator.get_page(page)
    listno = list.paginator.num_pages

    return render(request,'exam.html',{'q_list':list,'non_all':listno})


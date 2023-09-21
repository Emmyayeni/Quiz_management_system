from django.shortcuts import render
from .models import Questions, AnswerOptions
import json
from django.http import JsonResponse
import random
from django.core.paginator import Paginator


# Create your views here.

def home(request):
    return render(request, 'home.html')


def questions(request):
    question = Questions.objects.all()
    context = {"questions": question}
    return render(request, 'testapp/questions.html', context)


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

def register(request):
    data = json.loads(request.body)
    datas = data['form']
    print(datas)
    return JsonResponse('user info received', safe=False)



def question_create(request):
    questions = Questions.objects.all()

    # print(questions)
    # for questt in questions:
    #     print(questt)

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
    print(exam_list)
    return render(request,'exam.html',{'q_list':list,'non_all':listno})


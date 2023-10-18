from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'staff/home.html')

# def view_student(request):
#     return 
    
def create_test(request):
    # return test template here
    return render(request,'staff/snippets/create_test.html')

def student_list(request):
    return render(request,'staff/snippets/student.html')

def single_page(request):
    return render(request,'staff/snippets/single_page.html')

def create_quiz(request):
    return render(request,'staff/snippets/create_quiz.html')
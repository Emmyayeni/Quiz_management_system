from account.models import Account, Student, Staff
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# faculty
class Faculty(models.Model):
    name = models.CharField(max_length=255)
    faculty_hod = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# school
class School(models.Model):
    name = models.CharField(max_length=255)
    faculties = models.ManyToManyField(Faculty)

    def __str__(self):
        return self.name


# Course
class Course(models.Model):
    name = models.CharField(max_length=255)
    lectures = models.ManyToManyField(Staff)

    def __str__(self):
        return self.name


# department
class Department(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    dept_hod = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name


# answer
class AnswerOptions(models.Model):
    a = models.CharField(max_length=255)
    b = models.CharField(max_length=255)
    c = models.CharField(max_length=255)
    d = models.CharField(max_length=255)

    def __str__(self):
        return f'a.{self.a}|b.{self.b}|c.{self.c}|d.{self.d}'


# questions
class Questions(models.Model):
    question = models.CharField(max_length=555)
    answer_options = models.ForeignKey(AnswerOptions, on_delete=models.CASCADE, null=True, blank=True)
    correct_answer = models.CharField(blank=True, max_length=255, null=True)
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


# test
class Test(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    question = models.ForeignKey(Questions,on_delete=models.DO_NOTHING)
    answer = models.CharField(max_length=255)
    score = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.course.name

    def calculate_test_score(self):
        if self.answer == self.question.correct_answer:
             self.score = 2
             return self.score
        else:
            self.score = 0
            return self.score

    
        
    

# studentquestionanswer
class StudentQuestAns(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    tests = models.ForeignKey(Test, on_delete=models.CASCADE, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.student.name

class TotalCourseTest(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    questions = models.ManyToManyField(Test,blank=True)
    total_score = models.IntegerField(blank=True,null=True)


    def __str__(self):
        return self.user.username

    def add_questions(self):
        course = self.course
        user= self.user
        all_q = Test.objects.filter(user=user,course=course)
        for q in all_q:
            self.questions.add(q)


    def calculate_total_score(self):
        questions = self.questions
        total = sum([q.score for q in questions.all()])
        return total

        


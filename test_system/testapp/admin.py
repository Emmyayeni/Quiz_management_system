from django.contrib import admin
from .models import AnswerOptions, Questions,StudentQuestAns,Test,Faculty,Department,Course
# Register your models here.
admin.site.register(Questions)
admin.site.register(StudentQuestAns)
admin.site.register(Test)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Course)



admin.site.register(AnswerOptions)
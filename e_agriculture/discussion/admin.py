from django.contrib import admin
from . models import Question,Answer
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('posted_by', 'question_text', 'date_posted')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
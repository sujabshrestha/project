from django.shortcuts import render,redirect
from django.views.generic import ListView,CreateView
from . models import Question,Answer
# Create your views here.

def questions(request):
    current_user = request.user.username

    discuss = Question.objects.all()

    context = {'questions': discuss}
    return render(request, 'discussion/Question_form.html', context)


def question(request):
    current_user = request.user.username

    if request.method == 'POST':

        c_user = current_user
        question =  request.POST.get('question','')

        if question != '':
            query = Question(question_text=question, posted_by=c_user)
        
            query.save()
        else:
            print('error')

    return redirect('questions')



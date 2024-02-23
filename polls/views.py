from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question
from django.shortcuts import render,  get_object_or_404 ,redirect
from .forms import StudentForm
from django.contrib import messages
from .models import Student

# Create your views here.
# def index(request,name):
#     return HttpResponse(name)

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def members(request):
    return HttpResponse("Hello world!")

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def userform(request):
    sum=0
    try:    
        n1 = int(request.POST.get('value1'))
        n2 = int(request.POST.get('value2'))
        sum = n1+n2
    except:
       pass
    return render(request,'userform.html',{'output':sum})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, 'Student added successfully!')       
            return redirect('addstudent') 
        else:
            students = Student.objects.all()
            print(form.errors)
            return render(request, 'add_student.html', {'form': form, 'students': students})
    else:
        form = StudentForm()
        print(form)
    students = Student.objects.all()
    return render(request, 'add_student.html', {'form': form, 'students': students})

def edit(request,id):
    student_instance = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student_instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student record updated successfully!')
            return redirect('addstudent') 
    else:
        form = StudentForm(instance=student_instance)
    return render(request, 'edit.html', {'form': form})

def delete(request,id):
    student_instance = get_object_or_404(Student, id=id)
    student_instance.delete()
    messages.success(request, 'Student record deleted successfully!')
    return redirect('addstudent')  
   
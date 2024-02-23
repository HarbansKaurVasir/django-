from django.http import HttpResponse
from django.shortcuts import render

def aboutus(request):
    return HttpResponse("THIS IS ABOUT PAGE") 

def homepage(request):
    data = {
        'title' :'home page',
        'content' : 'here is the content',
        'list': ['php','django','css'],
        'numbers':[1,2,3,4,5,67,],
        'dic':[
            {'name':'pardeep','no':668697},
            {'name':'harman','no':6686979344}
        ]
    }
    return render(request,"index.html",data)
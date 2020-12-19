from django.shortcuts import render
from onlineexam.models import Exam

def examonline(request):
    return render(request, "base.html")

def quiz(request):
    results=Exam.objects.all()
    return render(request, "Index.html", {"Exam":results} )
    
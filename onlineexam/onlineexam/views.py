from django.shortcuts import render
from onlineexam.models import Exam
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def examonline(request):
    return render(request, "base.html")

def quiz(request):
    results=Exam.objects.all()

    #paginator=Paginator(results, 1)
    # page=request.GET.get("page")
    # try:
    #     results=paginator.page(page)
    # except PageNotAnInteger:
    #     results=paginator.page(1)
    # except EmptyPage:
    #     results=paginator.page(paginator.num_pages )
    return render(request, "Index.html", {"Exam":results})
    
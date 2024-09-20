from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import *

def index(request):
    jobs = Job.objects.all()

    context = {
        "jobs": jobs,
    }

    return render(request, "base.html", context)


def detail(request, id):
    job = get_object_or_404(Job, id=id)

    context = {
        "job": job,
        "title": job.title,
        "salary": job.salary,
        "description": job.description,
    }

    return render(request, "detail.html", context)


def my_jobs(request):
    selected_jobs = Job.objects.filter(selected=True)

    return render(request, "my_jobs.html", {"jobs": selected_jobs})


def save_job(request, id):
    job = get_object_or_404(Job, id=id)
    job.selected = True
    job.save()

    return HttpResponseRedirect("/my-jobs/")


def delete_job(request, id):
    job = get_object_or_404(Job, id=id)
    job.selected = False
    job.save()

    my_jobs = Job.objects.filter(selected=True)
    
    return render(request, "my_jobs.html", {"jobs": my_jobs})
 

def add(request):
    if request.method == "POST":
        title = request.POST["title"]
        descr = request.POST["descr"]
        salary = request.POST["salary"]
        photo = request.FILES.get("img")
        cat = request.POST["cat"]

        if photo:
            Job.objects.create(title=title, description=descr, salary=salary, image=photo, category=cat)

            return HttpResponseRedirect("/")
    

    return render(request, "add.html", {})
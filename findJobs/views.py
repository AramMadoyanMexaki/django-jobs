from django.shortcuts import render
from django.http import HttpResponse
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


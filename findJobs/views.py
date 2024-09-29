from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

from .models import *


def index(request):
    
    if request.user.is_authenticated:
        jobs = Job.objects.all()
        username = request.user.username

        context = {
            "jobs": jobs,
            "username": username,
        }
    else:
        username = None

        context = {}

    return render(request, "base.html", context)


def detail(request, id):
    job = get_object_or_404(Job, id=id)

    image = job.image.url if job.image else None

    context = {
        "job": job,
        "title": job.title,
        "salary": job.salary,
        "description": job.description,
        "image": image,
        "country": job.country,
    }

    return render(request, "detail.html", context)


def my_jobs(request):
    if request.user.is_authenticated:
        selected_jobs = Job.objects.filter(selected_by=request.user)

        job = None
        j = 0
        if selected_jobs:  # Check if there are any jobs
            while j < len(selected_jobs):
                job = selected_jobs[j]
                j += 1

        # Render template only if there is at least one job with an image
        if job and job.image:
            return render(request, "my_jobs.html", {"jobs": selected_jobs, "img": job.image.url})
        
        # Render without image if no job has an image
        return render(request, "my_jobs.html", {"jobs": selected_jobs})

    return HttpResponseRedirect("/login/")


def save_job(request, id):
    if request.user.is_authenticated:
        job = get_object_or_404(Job, id=id)
        job.selected_by.add(request.user)  # Add user to selected_by
        job.selected = True
        job.save()

        return HttpResponseRedirect("/my-jobs/")
    
    return HttpResponseRedirect("/login/")


def delete_job(request, id):
    if request.user.is_authenticated:
        job = get_object_or_404(Job, id=id) 
        job.selected = False
        job.save()

        my_jobs = Job.objects.filter(selected=True)
    
        return render(request, "my_jobs.html", {"jobs": my_jobs})
    
    return HttpResponseRedirect("/login/")
 

def add(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            title = request.POST.get("title", "")
            descr = request.POST.get("descr", "")
            salary = request.POST.get("salary", "")
            photo = request.FILES.get("img")
            cat_name = request.POST.get("cat", "")
            country = request.POST.get("country", "")
            
            try:
                category = Category.objects.get(name=cat_name)
            except Category.DoesNotExist:
                return render(request, "add.html", {"error": "Category does not exist"})

            if photo:
                Job.objects.create(title=title, country=country, description=descr, salary=salary, image=photo, category=category)
            else:
                Job.objects.create(title=title, country=country, description=descr, salary=salary, category=category)

            return HttpResponseRedirect("/")
        
        return render(request, "add.html", {})
    
    return HttpResponseRedirect("/login/")


def find(request):
    if request.method == "GET":
        render(request, "find.html", {})

    search = request.GET.get("search", "").strip()
    jobs = Job.objects.all()

    if search:
        finded_jobs = jobs.filter(category__name__icontains=search)
    else:
        finded_jobs = jobs

    context = {
        "jobs": finded_jobs,
    }

    return render(request, "find.html", context)


def _login(request):
    if request.method == "POST":
        password = request.POST["password"]
        email = request.POST["email"]
        username = request.POST["username"]

        user = authenticate(request, password=password, email=email, username=username)

        if user:
            login(request, user)
            return HttpResponseRedirect("/")

    return render(request, "login.html", {})


def registrate(request):
    if request.method == "GET":
        return render(request, "registrate.html", {})

    password = request.POST.get("password")
    username = request.POST.get("username")
    name = request.POST.get("name")
    lastname = request.POST.get("lastname")
    email = request.POST.get("email")
    country = request.POST.get("country")
    age = int(request.POST.get("age"))

    user = User.objects.create(
        username=username,
        email=email,
        password=make_password(password)
    )

    JobUser.objects.create(
        user=user,
        name=name,
        lastname=lastname,
        age=age,
        country=country
    )

    return HttpResponseRedirect("/login/")


def log_out(request):
    logout(request)
    return HttpResponseRedirect("/login/")
    
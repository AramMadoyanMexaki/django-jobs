from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path("details/<int:id>/", views.detail, name="details"),
    path('save-job/<int:id>/', views.save_job, name='save_job'),
    path("my-jobs/", views.my_jobs, name="my_jobs")
]
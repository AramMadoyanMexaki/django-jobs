from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path("details/<int:id>/", views.detail, name="details"),
    path("save-job/<int:id>/", views.save_job, name='save_job'),
    path("delete-job/<int:id>/", views.delete_job, name="delete"),
    path("my-jobs/", views.my_jobs, name="my_jobs"),
    path("add/", views.add, name="add_job"),
    path("login/", views._login, name="login"),
    path("log-out/", views.log_out, name="log_out"),
    path("registrate/", views.registrate, name="registrate"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
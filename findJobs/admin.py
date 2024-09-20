from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class JobAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "salary", "created_at", "updated_at", "category")


# class UserAdmin(admin.ModelAdmin):
#     list_display = ("id", "name", "lastname", "country", "age")

admin.site.register(Category, CategoryAdmin)
admin.site.register(Job, JobAdmin)
# admin.site.register(JobUser, UserAdmin)
from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class JobAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "salary", "country", "created_at", "updated_at", "category", "image")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Job, JobAdmin)

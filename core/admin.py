from django.contrib import admin
from .models import Category, Service


# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "meta_title", "service",]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Service, ServiceAdmin)

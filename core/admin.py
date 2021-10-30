from django.contrib import admin
from core.models import *

# Register your models here.
@admin.register(User)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('role',)
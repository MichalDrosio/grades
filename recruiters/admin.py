from django.contrib import admin
from recruiters.models import Recruiter
# Register your models here.


@admin.register(Recruiter)
class RecruiterAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
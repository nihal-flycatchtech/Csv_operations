from django.contrib import admin
from rest_csv.models import File


class FileAdmin(admin.ModelAdmin):
    list_display = ["id", "firstname", "lastname", "email", "profession"]


admin.site.register(File, FileAdmin)
from django.contrib import admin

# Register your models here.

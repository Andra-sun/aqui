from django.contrib import admin
from .models import Listinha
# Register your models here.
@admin.register(Listinha)
class ListinhaAdmin(admin.ModelAdmin):
    ...
from django.contrib import admin
from .models import PersonData

admin.site.site_header="DataFinder Adminastration"
admin.site.site_title="Admin-Dashboard"
admin.site.index_title="DataFinder Admin-Dashboard"
# Register your models here.

admin.site.register((PersonData))
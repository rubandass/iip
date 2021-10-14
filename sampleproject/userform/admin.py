from django.contrib import admin
from .models import Request
# Register your models here.

class RequestAdmin(admin.ModelAdmin):
    list_display = ("user", "server", "location", "contact_person","contact_number", "date", "status")
    list_filter = ("user", "server", "location", "date", "status")

admin.site.register(Request, RequestAdmin)
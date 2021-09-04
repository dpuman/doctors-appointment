from django.contrib import admin
from .models import *
# Register your models here.


class DoctorAdmin(admin.ModelAdmin):
    search_fields = ['email', "phone"]
    list_filter = ['phone', 'name']
    list_display = ['name', 'email', 'phone',
                    'degree', 'title', 'max_patient']
    list_per_page = 10


admin.site.register(Days)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Appointment)
admin.site.register(Prescription)

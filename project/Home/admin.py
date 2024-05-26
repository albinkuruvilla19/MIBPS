from django.contrib import admin
from .models import Staff,NewsNEvents,SchoolInfo,Class,Student,MandatoryDisclosure

# Register your models here.
admin.site.register(Staff)
admin.site.register(NewsNEvents)
admin.site.register(SchoolInfo)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(MandatoryDisclosure)
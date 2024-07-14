from django.contrib import admin
from .models import Staff,NewsNEvents,SchoolInfo,MandatoryDisclosure,Facility,Album,Image,AboutSchool,Management,BannerImage

# Register your models here.
admin.site.register(Staff)
admin.site.register(NewsNEvents)
admin.site.register(SchoolInfo)
admin.site.register(MandatoryDisclosure)
admin.site.register(Facility)
admin.site.register(Album)
admin.site.register(Image)
admin.site.register(AboutSchool)
admin.site.register(Management)
admin.site.register(BannerImage)
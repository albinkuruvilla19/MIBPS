from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import AbstractUser

class Staff(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='teacher_images/',blank=True,null=True)
    teaching_staff = models.BooleanField(default=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    address_line1 = models.CharField(max_length=255, blank=True, null=True)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)

    @classmethod
    def count_teaching_staff(cls):
        return cls.objects.filter(teaching_staff=True).count()

    @classmethod
    def count_non_teaching_staff(cls):
        return cls.objects.filter(teaching_staff=False).count()


    def __str__(self):
        return self.name

class NewsNEvents(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class SchoolInfo(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='school_logos/', blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    total_students = models.PositiveIntegerField(blank=True, null=True)
    total_transportation_vehicles = models.PositiveIntegerField(blank=True, null=True)
    total_classrooms = models.PositiveIntegerField(blank=True, null=True)

    phone = models.CharField(max_length=100, blank=True, null=True)
    address_line1 = models.CharField(max_length=255, blank=True, null=True)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    facebook_link = models.URLField(max_length=200, blank=True, null=True)
    youtube_link = models.URLField(max_length=200, blank=True, null=True)
    instagram_link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
    

class BannerImage(models.Model):
    image = models.ImageField(upload_to='banner_images/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Banner Image {self.id}"


class MandatoryDisclosure(models.Model):
    # Basic school details
    name_of_school = models.CharField(max_length=255)
    affiliation_no = models.CharField(max_length=100, blank=True, null=True)
    school_code = models.CharField(max_length=100, blank=True, null=True)
    complete_address = models.TextField()
    principal_name_and_qualification = models.CharField(max_length=255)
    school_email_id = models.EmailField()
    contact_details = models.CharField(max_length=100)

    # Documents
    copies_of_affiliation_letter = models.FileField(upload_to='documents/', blank=True, null=True)
    copies_of_societies_registration_certificate = models.FileField(upload_to='documents/', blank=True, null=True)
    copy_of_noc_issued_by_state_govt = models.FileField(upload_to='documents/', blank=True, null=True)
    copies_of_recognition_certificate = models.FileField(upload_to='documents/', blank=True, null=True)
    copy_of_valid_building_safety_certificate = models.FileField(upload_to='documents/', blank=True, null=True)
    copy_of_valid_fire_safety_certificate = models.FileField(upload_to='documents/', blank=True, null=True)
    copy_of_deo_certificate = models.FileField(upload_to='documents/', blank=True, null=True)
    copies_of_valid_water_health_sanitation_certificates = models.FileField(upload_to='documents/', blank=True, null=True)

    # Fee structure and academic details
    fee_structure_of_the_school = models.FileField(upload_to='documents/', blank=True, null=True)
    annual_academic_calendar = models.FileField(upload_to='documents/', blank=True, null=True)
    list_of_school_management_committee = models.FileField(upload_to='documents/', blank=True, null=True)
    list_of_parents_teachers_association_members = models.FileField(upload_to='documents/', blank=True, null=True)
    last_three_years_board_exam_results = models.FileField(upload_to='documents/', blank=True, null=True)

    # Number details
    principal = models.CharField(max_length=255)
    total_no_of_teachers = models.IntegerField()
    pgt_teachers = models.IntegerField()
    tgt_teachers = models.IntegerField()
    prt_teachers = models.IntegerField()
    teachers_section_ratio = models.CharField(max_length=255,null=True,blank=True)
    details_of_special_educator = models.TextField()
    details_of_counsellor_and_wellness_teacher = models.TextField()

    # Infrastructure details
    total_campus_area = models.FloatField()
    no_and_size_of_classrooms = models.TextField()
    no_and_size_of_laboratories = models.TextField()
    internet_facility = models.BooleanField(default=False)
    no_of_girls_toilets = models.IntegerField()
    no_of_boys_toilets = models.IntegerField()
    youtube_link_of_inspection_video = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name_of_school


class Facility(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='facility_images/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Album(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Image(models.Model):
    album = models.ForeignKey(Album, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class AboutSchool(models.Model):
    about_us = models.TextField()
    our_mission = models.TextField()
    our_vision = models.TextField()
    



class Management(models.Model):
    our_principal = models.CharField(max_length=100, blank=True, null=True)
    principal_image = models.ImageField(upload_to='images/', blank=True, null=True)
    principal_message = RichTextUploadingField(blank=True, null=True)  # New field for principal's message
    our_finance_manager = models.CharField(max_length=100, blank=True, null=True)
    finance_manager_image = models.ImageField(upload_to='images/', blank=True, null=True)
    our_local_manager = models.CharField(max_length=100, blank=True, null=True)
    local_manager_image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f"{self.our_principal or 'No Principal'}, {self.our_finance_manager or 'No Finance Manager'}, {self.our_local_manager or 'No Local Manager'}"


    
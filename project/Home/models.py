from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='teacher_images/',blank=True,null=True)
    teaching_staff = models.BooleanField(default=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    address_line1 = models.CharField(max_length=255, blank=True, null=True)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.name

class NewsNEvents(models.Model):
    title = models.CharField(max_length=200)
    content1 = models.TextField()
    content2 = models.TextField(blank=True,null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)

    def __str__(self):
        return self.title
    
class SchoolInfo(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='school_logos/', blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    address_line1 = models.CharField(max_length=255, blank=True, null=True)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    facebook_link = models.URLField(max_length=200, blank=True, null=True)
    youtube_link = models.URLField(max_length=200, blank=True, null=True)
    instagram_link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
    


class Class(models.Model):
    name = models.CharField(max_length=100)
    class_teacher = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True)
    students = models.ManyToManyField('Student', related_name='classes', blank=True)

    def __str__(self):
        return self.name
    
    def student_count(self):
        return self.students.count()


class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    admission_no = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, blank=True, null=True)
    religion = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    address_line1 = models.CharField(max_length=255, blank=True, null=True)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='student_images/', blank=True, null=True)
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100, blank=True, null=True)
    father_phone = models.CharField(max_length=100, blank=True, null=True)
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100, blank=True, null=True)
    mother_phone = models.CharField(max_length=100, blank=True, null=True)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


from django.db import models

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
    teachers_section_ratio = models.FloatField()
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

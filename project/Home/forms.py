from django import forms
from .models import NewsNEvents,Staff,SchoolInfo,MandatoryDisclosure

class NewsNEventsForm(forms.ModelForm):
    class Meta:
        model = NewsNEvents
        fields = ['title', 'content1', 'content2', 'image']


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'


class SchoolForm(forms.ModelForm):
    class Meta:
        model = SchoolInfo
        fields = '__all__'

class GeneralInfoForm(forms.ModelForm):
    class Meta:
        model = MandatoryDisclosure
        fields = ['name_of_school',"affiliation_no",'school_code','complete_address','principal_name_and_qualification','school_email_id','contact_details']

class DocumentsForm(forms.ModelForm):
    class Meta:
        model = MandatoryDisclosure
        fields = document_fields = ['copies_of_affiliation_letter', 'copies_of_societies_registration_certificate', 'copy_of_noc_issued_by_state_govt', 'copies_of_recognition_certificate', 'copy_of_valid_building_safety_certificate', 'copy_of_valid_fire_safety_certificate', 'copy_of_deo_certificate', 'copies_of_valid_water_health_sanitation_certificates']


class AcademicsForm(forms.ModelForm):
    class Meta:
        model = MandatoryDisclosure
        fields = ['fee_structure_of_the_school', 'annual_academic_calendar', 'list_of_school_management_committee', 'list_of_parents_teachers_association_members', 'last_three_years_board_exam_results']



class StatisticsForm(forms.ModelForm):
    class Meta:
        model = MandatoryDisclosure
        fields = ['principal', 'total_no_of_teachers', 'pgt_teachers', 'tgt_teachers', 'prt_teachers', 'teachers_section_ratio', 'details_of_special_educator', 'details_of_counsellor_and_wellness_teacher']


class InfrastructureForm(forms.ModelForm):
    class Meta:
        model = MandatoryDisclosure
        fields = ['total_campus_area', 'no_and_size_of_classrooms', 'no_and_size_of_laboratories', 'internet_facility', 'no_of_girls_toilets', 'no_of_boys_toilets', 'youtube_link_of_inspection_video']

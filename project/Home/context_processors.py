from .models import SchoolInfo

def school_info(request):
    school_info = SchoolInfo.objects.first()  # Assuming there's only one entry
    return {'school_info': school_info}
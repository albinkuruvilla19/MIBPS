from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewsNEventsForm,StaffForm,SchoolForm,GeneralInfoForm,FacilityForm,AlbumForm,ImageForm,AboutSchoolForm,ManagementForm,BannerForm,AdminLoginForm
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.utils.safestring import mark_safe

def index(request):
    banners = BannerImage.objects.all().order_by('-upload_date')
    teachers = Staff.objects.all()
    news = NewsNEvents.objects.all()
    teaching_count = Staff.count_teaching_staff()
    management = Management.objects.first()

    # Mark the principal message as safe
    if management:
        management.principal_message_safe = mark_safe(management.principal_message)
    else:
        management.principal_message_safe = ""  # Handle the case if no management object exists

    return render(request, 'index.html', {
        "teachers": teachers,
        "news": news,
        "teaching_count": teaching_count,
        "banners": banners,
        "management": management
    })

@login_required
def view(request):
    teachers = Staff.objects.all()
    teaching_count = Staff.count_teaching_staff()
    non_teaching_count = Staff.count_non_teaching_staff()
    context = {
        "teachers": teachers,
        "teaching_count": teaching_count,
        "non_teaching_count": non_teaching_count,
    }
    return render(request, "admin1/index.html", context)

@login_required
def add_news(request):
    if request.method == 'POST':
        form = NewsNEventsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_list')  # Redirect to the news list or any other desired page
    else:
        form = NewsNEventsForm()
    return render(request, 'admin1/add_news.html', {'form': form})

@login_required
def edit_news(request, pk):
    news = get_object_or_404(NewsNEvents, pk=pk)
    if request.method == 'POST':
        form = NewsNEventsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news_list')  # Redirect to the news list or any other desired page
    else:
        form = NewsNEventsForm(instance=news)
    return render(request, 'admin1/edit_news.html', {'form': form})

@login_required
def delete_news(request, pk):
    news = get_object_or_404(NewsNEvents, pk=pk)
    if request.method == 'POST':
        news.delete()
        return redirect('news_list')  # Redirect to the news list or any other desired page
    return render(request, 'admin1/delete_news.html', {'news': news})

@login_required
def news_list(request):
    news = NewsNEvents.objects.all().order_by('-published_date')
    return render(request, 'admin1/news_list.html', {'news': news})

@login_required
def staffs_list(request):
    staffs = Staff.objects.all()
    return render(request, 'admin1/staffs_list.html', {'staffs': staffs})

@login_required
def add_staffs(request):
    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('staffs_list')  # Redirect to the news list or any other desired page
    else:
        form = StaffForm()
    return render(request, 'admin1/add_staffs.html', {'form': form})

@login_required
def edit_staffs(request, pk):
    staffs = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES, instance=staffs)
        if form.is_valid():
            form.save()
            return redirect('staffs_list')  # Redirect to the news list or any other desired page
    else:
        form = StaffForm(instance=staffs)
    return render(request, 'admin1/edit_staffs.html', {'form': form})

@login_required
def delete_staffs(request, pk):
    staffs = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        staffs.delete()
        return redirect('staffs_list')  # Redirect to the news list or any other desired page
    return render(request, 'admin1/delete_staffs.html', {'staffs': staffs})

@login_required
def school_info(request):
    info = SchoolInfo.objects.first()
    if request.method == 'POST':
        form = SchoolForm(request.POST, request.FILES, instance=info)
        if form.is_valid():
            form.save()
            return redirect('school_info')  # Redirect to the news list or any other desired page
    else:
        form = SchoolForm(instance=info)
    return render(request, 'admin1/school_info.html', {'form': form})


from .forms import GeneralInfoForm, DocumentsForm, AcademicsForm, StatisticsForm, InfrastructureForm

@login_required
def mandatory_disclosure_update(request):
    general_info = MandatoryDisclosure.objects.first()
    
    if request.method == 'POST':
        general_form = GeneralInfoForm(request.POST, request.FILES, instance=general_info)
        documents_form = DocumentsForm(request.POST, request.FILES, instance=general_info)
        academics_form = AcademicsForm(request.POST, request.FILES, instance=general_info)
        statistics_form = StatisticsForm(request.POST, request.FILES, instance=general_info)
        infrastructure_form = InfrastructureForm(request.POST, request.FILES, instance=general_info)
        
        if general_form.is_valid() and documents_form.is_valid() and academics_form.is_valid() and statistics_form.is_valid() and infrastructure_form.is_valid():
            general_form.save()
            documents_form.save()
            academics_form.save()
            statistics_form.save()
            infrastructure_form.save()
            return redirect('mandatory_disclosure_update')  # Redirect to the news list or any other desired page
    else:
        general_form = GeneralInfoForm(instance=general_info)
        documents_form = DocumentsForm(instance=general_info)
        academics_form = AcademicsForm(instance=general_info)
        statistics_form = StatisticsForm(instance=general_info)
        infrastructure_form = InfrastructureForm(instance=general_info)
    
    return render(request, 'admin1/mandatory_disclosure.html', {
        'general_form': general_form,
        'documents_form': documents_form,
        'academics_form': academics_form,
        'statistics_form': statistics_form,
        'infrastructure_form': infrastructure_form,
    })



def mandatory_disclosure(request):
    content = MandatoryDisclosure.objects.first()
    return render(request,'mandatory_disclosure.html',{"content":content})


def about_us(request):
    about_us = AboutSchool.objects.first()
    return render(request,'about.html',{"about_us":about_us})


def staffs(request):
    our_staffs  = Staff.objects.all()
    return render(request,'staff.html',{"our_staffs":our_staffs})

def facility(request):
    facilities  = Facility.objects.all()
    return render(request,'facility.html',{"facilities":facilities})

def contact(request):
    return render(request,'contact.html')

@login_required
def add_facility(request):
    if request.method == 'POST':
        form = FacilityForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('facility_list')  # Redirect to the news list or any other desired page
    else:
        form = FacilityForm()
    return render(request, 'admin1/add_facility.html', {'form': form})

@login_required
def edit_facility(request, pk):
    facilities = get_object_or_404(Facility, pk=pk)
    if request.method == 'POST':
        form = FacilityForm(request.POST, request.FILES, instance=facilities)
        if form.is_valid():
            form.save()
            return redirect('facility_list')  # Redirect to the news list or any other desired page
    else:
        form = FacilityForm(instance=facilities)
    return render(request, 'admin1/edit_facility.html', {'form': form})

@login_required
def delete_facility(request, pk):
    facilities = get_object_or_404(Facility, pk=pk)
    if request.method == 'POST':
        facilities.delete()
        return redirect('facility_list')  # Redirect to the news list or any other desired page
    return render(request, 'admin1/delete_facility.html', {'facilities': facilities})

def facility_list(request):
    facilities = Facility.objects.all()
    return render(request, 'admin1/facility_list.html', {'facilities': facilities})

def gallery(request):
    albums = Album.objects.all()
    images = Image.objects.all().order_by('-uploaded_at')
    return render(request,'gallery.html',{"albums":albums,"images":images})

@login_required
def update_gallery(request):
    albums = Album.objects.all()
    images = Image.objects.all().order_by('-uploaded_at')
    return render(request,'admin1/update_gallery.html',{"albums":albums,"images":images})

@login_required
def add_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('update_gallery')  # Redirect to the news list or any other desired page
    else:
        form = ImageForm()
    return render(request, 'admin1/add_image.html', {'form': form})

@login_required
def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('update_gallery')  # Redirect to the news list or any other desired page
    else:
        form = AlbumForm()
    return render(request, 'admin1/add_album.html', {'form': form})


def album_list(request):
    albums = Album.objects.all()
    return render(request,'admin1/album_list.html',{"albums":albums})

@login_required
def delete_album(request, pk):
    albums = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        albums.delete()
        return redirect('album_list')  # Redirect to the news list or any other desired page
    return render(request, 'admin1/delete_album.html', {'albums': albums})

@login_required
def delete_image(request, pk):
    image = get_object_or_404(Image, pk=pk)
    if request.method == 'POST':
        image.delete()
        return redirect('update_gallery')  # Redirect to the news list or any other desired page
    return render(request, 'admin1/delete_image.html', {'image': image})

@login_required
def edit_about_us(request):
    about_us = AboutSchool.objects.first()
    if request.method == 'POST':
        form = AboutSchoolForm(request.POST, request.FILES, instance=about_us)
        if form.is_valid():
            form.save()
            return redirect('view')  # Redirect to the news list or any other desired page
    else:
        form = AboutSchoolForm(instance=about_us)
    return render(request, 'admin1/about_school.html', {'form': form})

@login_required
def edit_management(request):
    management = Management.objects.first()
    if request.method == 'POST':
        form = ManagementForm(request.POST, request.FILES, instance=management)
        if form.is_valid():
            form.save()
            return redirect('view')  # Redirect to the news list or any other desired page
    else:
        form = ManagementForm(instance=management)
    return render(request, 'admin1/edit_management.html', {'form': form})

def management(request):
    management = Management.objects.first()
    return render(request,'management.html',{"management":management})

@login_required
def edit_banner(request):
    banners = BannerImage.objects.all().order_by('-upload_date')
    return render(request,'admin1/edit_banner.html',{"banners":banners})

@login_required
def add_banner(request):
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('edit_banner')  # Redirect to the news list or any other desired page
    else:
        form = BannerForm()
    return render(request, 'admin1/add_banner.html', {'form': form})

@login_required
def delete_banner(request, pk):
    image = get_object_or_404(BannerImage, pk=pk)
    if request.method == 'POST':
        image.delete()
        return redirect('edit_banner')  # Redirect to the news list or any other desired page
    return render(request, 'admin1/delete_banner.html', {'image': image})



def principal_message(request):
    management = Management.objects.first()
    return render(request,'principal_message.html',{"management":management})


def ad_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_superuser:
                auth_login(request,user)
                messages.success(request, 'You have successfully logged in as a superuser.')
                return redirect('view')  # Redirect to the admin dashboard
            else:
                messages.error(request, 'You are not authorized to access this page.')
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'auth/login.html')


def logout_view(request):
    # Use the built-in logout function to log the user out
    logout(request)
    return redirect('index') 
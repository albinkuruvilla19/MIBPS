from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from .models import NewsNEvents
from .forms import NewsNEventsForm,StaffForm,SchoolForm,GeneralInfoForm
# Create your views here.
def index(request):
    teachers = Staff.objects.all()
    news = NewsNEvents.objects.all()
    info = SchoolInfo.objects.first()
    return render(request,'index.html',{"teachers":teachers,"news":news,"info":info},)

def view(request):
    teachers = Staff.objects.all()
    info = SchoolInfo.objects.first()
    classes = Class.objects.all()
    return render(request,"admin1/index.html",{"teachers":teachers,"info":info,"classes":classes})

def manage_classes(request):
    return render(request,'admin1/manage_classes.html')



def add_news(request):
    if request.method == 'POST':
        form = NewsNEventsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_list')  # Redirect to the news list or any other desired page
    else:
        form = NewsNEventsForm()
    return render(request, 'admin1/add_news.html', {'form': form})

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

def delete_news(request, pk):
    news = get_object_or_404(NewsNEvents, pk=pk)
    if request.method == 'POST':
        news.delete()
        return redirect('news_list')  # Redirect to the news list or any other desired page
    return render(request, 'admin1/delete_news.html', {'news': news})

def news_list(request):
    news = NewsNEvents.objects.all().order_by('-published_date')
    return render(request, 'admin1/news_list.html', {'news': news})

def staffs_list(request):
    staffs = Staff.objects.all()
    return render(request, 'admin1/staffs_list.html', {'staffs': staffs})


def add_staffs(request):
    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('staffs_list')  # Redirect to the news list or any other desired page
    else:
        form = StaffForm()
    return render(request, 'admin1/add_staffs.html', {'form': form})


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

def delete_staffs(request, pk):
    staffs = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        staffs.delete()
        return redirect('staffs_list')  # Redirect to the news list or any other desired page
    return render(request, 'admin1/delete_staffs.html', {'staffs': staffs})


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
    return render(request,'about.html')
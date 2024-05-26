from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('view/',views.view,name="view"),
    path('manage/',views.manage_classes,name="manage"),
    path('news/',views.news_list,name="news_list"),
    path('addnews/', views.add_news, name='add_news'),
    path('editnews/<int:pk>/', views.edit_news, name='edit_news'),
    path('deletenews/<int:pk>/', views.delete_news, name='delete_news'),
    path('staffs/',views.staffs_list,name="staffs_list"),
    path('addstaffs/', views.add_staffs, name='add_staffs'),
    path('editstaffs/<int:pk>/', views.edit_staffs, name='edit_staffs'),
    path('deletestaffs/<int:pk>/', views.delete_staffs, name='delete_staffs'),
    path('school_info/',views.school_info,name="school_info"),
    path('mandatory_disclosure_update/',views.mandatory_disclosure_update,name="mandatory_disclosure_update"),
    path('mandatory_disclosure/',views.mandatory_disclosure,name="mandatory_disclosure"),
    path('about_us/',views.about_us,name="about_us")
]
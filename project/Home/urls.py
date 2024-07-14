from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('view/',views.view,name="view"),
    path('news/',views.news_list,name="news_list"),
    path('addnews/', views.add_news, name='add_news'),
    path('editnews/<int:pk>/', views.edit_news, name='edit_news'),
    path('deletenews/<int:pk>/', views.delete_news, name='delete_news'),
    path('staffs_list/',views.staffs_list,name="staffs_list"),
    path('addstaffs/', views.add_staffs, name='add_staffs'),
    path('editstaffs/<int:pk>/', views.edit_staffs, name='edit_staffs'),
    path('deletestaffs/<int:pk>/', views.delete_staffs, name='delete_staffs'),
    path('school_info/',views.school_info,name="school_info"),
    path('mandatory_disclosure_update/',views.mandatory_disclosure_update,name="mandatory_disclosure_update"),
    path('mandatory_disclosure/',views.mandatory_disclosure,name="mandatory_disclosure"),
    path('about_us/',views.about_us,name="about_us"),
    path('staffs/',views.staffs,name="staffs"),
    path('facility/',views.facility,name="facility"),
    path('contact/',views.contact,name="contact"),

    path('facility_list/',views.facility_list,name="facility_list"),
    path('add_facility/', views.add_facility, name='add_facility'),
    path('edit_facility/<int:pk>/', views.edit_facility, name='edit_facility'),
    path('delete_facility/<int:pk>/', views.delete_facility, name='delete_facility'),
    path('gallery/',views.gallery,name="gallery"),
    path('update_gallery/',views.update_gallery,name="update_gallery"),
    path('add_image/',views.add_image,name="add_image"),
    path('add_album/',views.add_album,name="add_album"),
    path('album_list/',views.album_list,name="album_list"),
    path('delete_album/<int:pk>/', views.delete_album, name='delete_album'),
    path('delete_image/<int:pk>/', views.delete_image, name='delete_image'),
    path('admin1/about_school/',views.edit_about_us,name="about_school"),
    path('admin1/edit_management/',views.edit_management,name="edit_management"),
    path('management/',views.management,name="management"),
    path('edit_banner/',views.edit_banner,name="edit_banner"),
    path('add_banner/',views.add_banner,name="add_banner"),
    path('delete_banner/<int:pk>/', views.delete_banner, name='delete_banner'),
    
    path('principal_message/',views.principal_message,name='principal_message_detail'),
    path('mibps_admin/',views.ad_login,name="admin_login"),
    path('logout/',views.logout_view,name="logout")


]
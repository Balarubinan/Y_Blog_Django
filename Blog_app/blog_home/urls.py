from django.urls import include,path
from . import views
urlpatterns = [
    path('create/',views.show_blog_create),
    path('adminpage/',views.show_dashboard),
    path('adminlogin/',views.show_login),
    path('adminprofile/',views.show_profile)
]
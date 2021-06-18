from django.urls import include,path
from . import views
# template parameter -> <int:val_name> <string:val_name>
urlpatterns = [
    path('create/<str:name>/',views.show_blog_create,name='create'),
    path('adminpage/',views.show_dashboard),
    path('adminlogin/',views.show_login),
    path('adminprofile/',views.show_profile)
]
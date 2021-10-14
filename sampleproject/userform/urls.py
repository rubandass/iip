from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formvalues/', views.formvalues, name='formvalues'),
    path('status/', views.update_status, name='update_status'),
    path('getstatus/', views.get_status, name='get_status'),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r'^login', views.pagelogin, name='login'),
    url(r'^logout', views.pagelogout, name='logout'),
]

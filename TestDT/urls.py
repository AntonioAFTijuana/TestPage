#from django.urls import path
from . import views
from TestDT import views
from django.contrib import admin
from django.urls import path, include  # new
from django.views.generic.base import TemplateView  # new


urlpatterns = [
    path('',views.home),
    path('equipos/',views.equipos),
    path('users/',views.users),
    path('Model/',views.Model),
    path('NewModel/',views.Create_Model),
    path("administrator/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  # new
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]
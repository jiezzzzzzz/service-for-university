"""
URL configuration for university project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from admin_service.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('university/admin/', include('service.urls')),
    path('university/curator/', include('admin_service.urls')),
    path('start_generate_report/', start_generate_report, name='start_generate_report'),
    path('show_generate_report_status/<str:task_id>/', show_generate_report_status, name='show_generate_report_status'),
    path('get_report/<str:task_id>/', get_report, name='get_report'),

]

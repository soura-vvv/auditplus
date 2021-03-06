"""auditplus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    #path('department',views.departmentApi),
    #path(r'^department/([0-9]+)$',views.departmentApi),
    # path('admin/', admin.site.urls),
    path('get_sectors',views.get_sectors),
    path('add_user_question',views.add_user_question),
    path('get_questions',views.get_questions),
    path('add_user_sector',views.add_user_sector),
    path('register',views.register),
    path('login',views.login),
    path('get_user_questions',views.get_user_questions),
    
]

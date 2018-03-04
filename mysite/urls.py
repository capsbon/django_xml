"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,re_path
from vacancy.views import vacancy_index
from vacancy.views import vacancy_edit, login, logout, export_csv


urlpatterns = [
    path('admin/', admin.site.urls),
    path('vacancies/', vacancy_index, name='vacancy_index'),
    re_path(r'^vacancies/edit/(.+)/$', vacancy_edit, name='vacancy_edit'),
    path('vacancies/login/', login, name='login'),
    path('vacancies/logout/', logout, name='logout'),
    path('vacancies/export/', export_csv, name='export_csv'),

]

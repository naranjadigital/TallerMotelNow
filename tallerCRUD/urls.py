"""tallerCRUD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from motelnow.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('backoffice/', backoffice, name='backoffice'),
    path('backoffice/hostal/create', HostalCreate.as_view(), name='hostal-create'),
    path('backoffice/hostal/', HostalList.as_view(), name='hostal-list'),
    path('backoffice/hostal/<int:pk>/delete/', HostalDelete.as_view(), name='hostal-delete'),
    path('backoffice/hostal/<int:pk>/update/', HostalUpdate.as_view(), name='hostal-update'),
]

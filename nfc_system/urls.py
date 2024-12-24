"""
URL configuration for nfc_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from frontend import views  # Make sure the frontend views are correctly imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Root URL should use the home view
    path('login/', views.login_view, name='login'),
    path('superuser/', views.superuser_dashboard, name='superuser_dashboard'),
    path('manager/', views.manager_dashboard, name='manager_dashboard'),
    path('assign-task/', views.assign_task, name='assign_task'),
    path('unassign-task/<int:task_id>/', views.unassign_task, name='unassign_task'),
]





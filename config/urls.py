"""
URL configuration for config project.

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
from django.urls import path, include
# from watchlist.api.views import students, student_details
from watchlist.api.views import StudentDetailsAv, StudentsAv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include('watchlist.api.urls')),
    path('students/', StudentsAv.as_view(), name='students'),
    path('students/<int:pk>/', StudentDetailsAv.as_view(), name='student-details')
]

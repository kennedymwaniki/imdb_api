
from django.contrib import admin
from django.urls import path, include
# from watchlist.api.views import students, student_details
from watchlist.api.views import StudentDetailsAv, StudentsAv, StudentViewSet
from rest_framework.routers import DefaultRouter
from django.shortcuts import redirect
router = DefaultRouter()

router.register('students', StudentViewSet, basename='students')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include('watchlist.api.urls')),
    # path('students/', StudentsAv.as_view(), name='students'),
    # path('students/<int:pk>/', StudentDetailsAv.as_view(), name='student-details'),
    path('', lambda request: redirect('students-list', permanent=False)),
    path("", include(router.urls)),
    # path('api-auth/', include('rest_framework.urls')),
]

from django.contrib import admin
from .models import WatchList, Student, StreamPlatform, Review
# Register your models here.
admin.site.register(WatchList)
admin.site.register(Student)
admin.site.register(StreamPlatform)
admin.site.register(Review)

from django.contrib import admin
from .models import Profile, LessonPlan, Subject
# Register your models here.

admin.site.register(Profile)
admin.site.register(LessonPlan)
admin.site.register(Subject)
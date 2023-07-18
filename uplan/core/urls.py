from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import index, create_lesson
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.create_lesson, name='create_lesson'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
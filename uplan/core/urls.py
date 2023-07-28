from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import index, create_lesson, lesson_view, search, UpdateLesson, create_pdf
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.create_lesson, name='create_lesson'),
    path('lesson/<str:slug>/', views.lesson_view, name='lesson_view'),
    path('search', views.search, name='search_results'),
    path('lesson/update/<str:slug>/', UpdateLesson.as_view(), name='update_lesson'),
    path('generate/pdf/<str:slug>/', views.create_pdf, name='create_pdf')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
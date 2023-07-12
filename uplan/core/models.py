from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    given_name = models.CharField(max_length=256, blank=True, null=True)
    family_name = models.CharField(max_length=256, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    lesson_plans = models.ManyToManyField("LessonPlan", related_name="lesson_plan", blank=True)

    def __str__(self):
        return f"{self.given_name} {self.family_name}"

    def save(self, *args, **kwargs):
        # self.primary_teacher =
        super(Profile, self).save(*args, **kwargs)
        pass

class LessonPlan(models.Model):
    primary_teacher = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.SET_NULL, related_name="teacher")
    associated_teachers = models.ManyToManyField(Profile, related_name="associated_teachers", blank=True)
    subject = models.OneToOneField("Subject", on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=256, null=True, blank=True)
    text_content = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    lesson_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

class Subject(models.Model):
    name = models.CharField(max_length=256)
    teacher = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.SET_NULL, related_name="lesson_teacher")
    primary_colour = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.teacher.given_name} {self.teacher.family_name}'s {self.name} class"
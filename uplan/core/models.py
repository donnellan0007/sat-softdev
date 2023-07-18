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

    def save(self):
        print("Profile saved")

class LessonPlan(models.Model):
    primary_teacher = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.SET_NULL, related_name="teacher")
    associated_teachers = models.ManyToManyField(Profile, related_name="associated_teachers")
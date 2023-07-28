from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
import uuid

from .validators import validate_existence


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    given_name = models.CharField(max_length=256, blank=True, null=True)
    family_name = models.CharField(max_length=256, blank=True, null=True)
    is_admin = models.BooleanField(default=False)

    @property
    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    def __str__(self):
        return f"{self.given_name} {self.family_name}"

    def save(self, *args, **kwargs):
        # self.primary_teacher =
        super(Profile, self).save(*args, **kwargs)
        pass

class LessonPlan(models.Model):
    primary_teacher = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.SET_NULL, related_name="lessons")
    associated_teachers = models.ManyToManyField(Profile, related_name="associated_teachers", blank=True)
    subject = models.ManyToManyField("Subject", blank=True, related_name='lesson_plan')
    title = models.CharField(max_length=256, null=True, blank=True, validators=[validate_existence])
    text_content = models.TextField(blank=False, null=False, validators=[validate_existence])
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    lesson_date = models.DateField(blank=True, null=True)
    slug = models.SlugField(
        default='',
        editable=True,
        max_length=75,
        unique=True,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title
    def get_slug(self):
        uuid_value = str(uuid.uuid4())
        unique_slug = slugify(uuid_value[0:12])
        return unique_slug

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug,
        }
        return reverse('core:lesson_view', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.title
        if not self.slug:
            self.slug = self.get_slug()
        super().save(*args, **kwargs)

class Subject(models.Model):
    name = models.CharField(max_length=256)
    teacher = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.SET_NULL, related_name="subjects")
    primary_colour = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.teacher.given_name} {self.teacher.family_name}'s {self.name} class"
from django import forms
from .models import Profile, LessonPlan

class LessonPlanForm(forms.ModelForm):
    class Meta:
        model = LessonPlan
        fields = ["title", "text_content", "lesson_date"]
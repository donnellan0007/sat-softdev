from django import forms
from .models import Profile, LessonPlan

class LessonPlanForm(forms.ModelForm):
    class Meta:
        model = LessonPlan
        fields = ["title", "text_content", "subject", "lesson_date"]
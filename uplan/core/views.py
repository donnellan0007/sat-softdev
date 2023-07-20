from django.shortcuts import render, redirect
from .forms import LessonPlanForm
from .models import Profile, LessonPlan, Subject
# Create your views here.
def index(request):
    cur_user = request.user.profile
    user_subjects = cur_user.subjects.all()
    lesson_plans = cur_user.lessons.all()
    context = {
        'subjects': user_subjects,
        'lessons': lesson_plans
    }
    return render(request, 'core/index.html', context)

def lesson_view(request, slug):
    lesson = LessonPlan.objects.get(slug=slug)
    context = {
        'lesson': lesson
    }
    return render(request, 'core/lesson_view.html', context)

def create_lesson(request):
    if request.method == 'POST':
        form = LessonPlanForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.primary_teacher = request.user.profile
            obj.save()
            return redirect('core:index')
    else:
        form = LessonPlanForm()
    return render(request, 'core/create_lesson.html', {'form':form})

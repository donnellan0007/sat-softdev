from django.shortcuts import render, redirect
from .forms import LessonPlanForm
# Create your views here.
def index(request):
    return render(request, 'core/index.html')

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

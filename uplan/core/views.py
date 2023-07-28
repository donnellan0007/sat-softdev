from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import UpdateView

from .forms import LessonPlanForm
from .models import Profile, LessonPlan, Subject
import io
# Import PDF Stuff
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
# Create your views here.
@login_required # ensures only logged in users can view the page
def index(request):
    cur_user = request.user.profile
    user_subjects = cur_user.subjects.all()
    lesson_plans = cur_user.lessons.all()
    context = {
        'subjects': user_subjects,
        'lessons': lesson_plans
    }
    return render(request, 'core/index.html', context)

def search(request):
    cur_user = request.user.profile
    user_subjects = cur_user.subjects.all()
    lesson_plans = cur_user.lessons.all()
    if request.GET:
        """
        The following gets the data sent from the form
        The data is retrieved through the "name" in the HTML
        """
        query = request.GET.get("q")
        date_start = request.GET.get("ds")
        date_end = request.GET.get("de")
        print(date_start, date_end)
        if date_start and date_end:
            searches = LessonPlan.objects.filter(
                Q(title__icontains=query) & Q(subject__teacher=cur_user) & Q(lesson_date__range=[date_start, date_end])
            ).order_by("-lesson_date")
        else:
            """
            Filtering the lesson plans where the title
            matches/contains the title
            Ensures only the current teacher's
            lessons are retrieved
            """
            searches = LessonPlan.objects.filter(
                Q(title__icontains=query) & Q(subject__teacher=cur_user)
            )

        context = {
            'results': searches,
            'query': query,
            'date_start': date_start,
            'date_end': date_end,
            'subjects': user_subjects,
            'lessons': lesson_plans
        }
    else:
        context = {}
    return render(request, 'core/search_results.html', context)
def lesson_view(request, slug):
    # in the urls.py file, the slug is used to
    #get the lesson plan itself
    lesson = LessonPlan.objects.get(slug=slug)
    context = {
        'lesson': lesson
    }
    return render(request, 'core/lesson_view.html', context)

def create_lesson(request):
    if request.method == 'POST':
        form = LessonPlanForm(request.POST)
        if form.is_valid():
            """ 
            we set commit=False due to the way in which the
            database and Django handles manytomany relations
            """
            obj = form.save(commit=False)
            obj.primary_teacher = request.user.profile
            obj.save()
            form.save_m2m()
            return redirect('core:index')
    else:
        form = LessonPlanForm()
    return render(request, 'core/create_lesson.html', {'form':form})


from textwrap import wrap

def create_pdf(request, slug):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 10)
    lesson = LessonPlan.objects.get(slug=slug)
    file_name = f"{lesson.title} - {lesson.lesson_date}.pdf"
    lines = []

    wrapped_text = "\n".join(wrap(lesson.text_content, 100))  # 80 is line width
    lines.append(f"{lesson.title} - {lesson.lesson_date}")
    lines.append("\n")
    lines.append("-------")
    lines.append("\n")
    lines.append(wrapped_text)
    lines.append("\n")

    # Loop
    for line in lines:
        textob.textLines(line)

    # Finish Up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    # Return something
    return FileResponse(buf, as_attachment=True, filename=file_name)
class UpdateLesson(UpdateView):
    model = LessonPlan
    fields = ['title', 'subject', 'text_content', 'lesson_date']
    template_name_suffix = '_update_form'
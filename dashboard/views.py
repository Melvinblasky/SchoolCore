from django.shortcuts import render
from students.models import Student
from teachers.models import Teacher
from academics.models import ClassRoom, Subject
from attendance_app.models import Attendance


def dashboard(request):

    context = {
        'students_count': Student.objects.count(),
        'teachers_count': Teacher.objects.count(),
        'classes_count': ClassRoom.objects.count(),
        'subjects_count': Subject.objects.count(),
    }

    return render(
        request,
        'dashboard/index.html',
        context
    )

present_count = Attendance.objects.filter(
    status='PRESENT'
).count()

absent_count = Attendance.objects.filter(
    status='ABSENT'
).count()

late_count = Attendance.objects.filter(
    status='LATE'
).count()

excused_count = Attendance.objects.filter(
    status='EXCUSED'
).count()
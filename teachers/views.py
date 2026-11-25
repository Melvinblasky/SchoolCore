from django.shortcuts import render, get_object_or_404
from .models import Teacher


def teacher_list(request):

    teachers = Teacher.objects.all()

    return render(
        request,
        'teachers/list.html',
        {
            'teachers': teachers
        }
    )


def teacher_detail(request, pk):

    teacher = get_object_or_404(
        Teacher,
        pk=pk
    )

    return render(
        request,
        'teachers/detail.html',
        {
            'teacher': teacher
        }
    )

from students.models import Student


def teacher_dashboard(request, pk):

    teacher = get_object_or_404(
        Teacher,
        pk=pk
    )

    total_students = Student.objects.count()

    context = {
        'teacher': teacher,
        'total_students': total_students,
    }

    return render(
        request,
        'teachers/dashboard.html',
        context
    )
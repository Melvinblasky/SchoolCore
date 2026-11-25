from django.shortcuts import render, redirect , get_object_or_404
from students.models import Student
from academics.models import Subject, ClassRoom
from django.db.models import Avg, Sum
from .models import Result, Examination
from .forms import ResultForm
from school.models import School
from decimal import Decimal
from attendance_app.models import Attendance

def result_list(request):

    results = Result.objects.all()

    return render(
        request,
        'results/list.html',
        {
            'results': results
        }
    )


def result_create(request):

    if request.method == "POST":

        form = ResultForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect(
                'result_list'
            )

    else:

        form = ResultForm()

    return render(
        request,
        'results/form.html',
        {
            'form': form
        }
    )

def report_card(request, student_id):

    student = get_object_or_404(
        Student,
        id=student_id
    )

    results = Result.objects.filter(
        student=student
    )

    average = results.aggregate(
        Avg('total_score')
    )['total_score__avg'] or 0

    total_score = results.aggregate(
        Sum('total_score')
    )['total_score__sum'] or 0

    total_subjects = results.count()

    # Get all students in same class
    class_students = Student.objects.filter(
        classroom=student.classroom
    )

    rankings = []

    for stu in class_students:

        stu_average = Result.objects.filter(
            student=stu
        ).aggregate(
            Avg('total_score')
        )['total_score__avg'] or 0

        rankings.append({
            'student': stu,
            'average': stu_average
        })

    rankings.sort(
        key=lambda x: x['average'],
        reverse=True
    )

    position = 0

    for index, item in enumerate(
        rankings,
        start=1
    ):

        if item['student'].id == student.id:

            position = index
            break

    # Display 1st, 2nd, 3rd, 4th...

    if position % 100 in [11, 12, 13]:

        position_display = f"{position}th"

    else:

        suffix = {
            1: "st",
            2: "nd",
            3: "rd"
        }.get(position % 10, "th")

        position_display = (
            f"{position}{suffix}"
        )

        total_days = Attendance.objects.filter(
        student=student
    ).count()

    present_days = Attendance.objects.filter(
        student=student,
        status='PRESENT'
    ).count()

    absent_days = Attendance.objects.filter(
        student=student,
        status='ABSENT'
    ).count()

    late_days = Attendance.objects.filter(
        student=student,
        status='LATE'
    ).count()

    attendance_percentage = 0
    if total_days > 0:

     attendance_percentage = round(
        (present_days / total_days) * 100,
        2
    )

    context = {

        'student': student,

        'results': results,

        'average': average,

        'total_score': total_score,

        'total_subjects': total_subjects,

        'position': position,

        'position_display': position_display,

        'total_days': total_days,

        'present_days': present_days,

        'absent_days': absent_days,

        'late_days': late_days,

        'attendance_percentage': attendance_percentage,

    }

    return render(
        request,
        'results/report_card.html',
        context
    )

def bulk_result_entry(request):

    classes = ClassRoom.objects.all()

    subjects = Subject.objects.all()

    exams = Examination.objects.all()

    selected_class = None

    students = []

    class_id = request.GET.get('class')

    if class_id:

        selected_class = ClassRoom.objects.get(
            id=class_id
        )

        students = Student.objects.filter(
            classroom=selected_class
        )

    if request.method == "POST":

        class_id = request.POST.get('class')

        subject_id = request.POST.get('subject')

        exam_id = request.POST.get('exam')

        selected_class = ClassRoom.objects.get(
            id=class_id
        )

        students = Student.objects.filter(
            classroom=selected_class
        )

        subject = Subject.objects.get(
            id=subject_id
        )

        exam = Examination.objects.get(
            id=exam_id
        )

        for student in students:

            ca = request.POST.get(
                f'ca_{student.id}'
            )

            exam_score = request.POST.get(
                f'exam_{student.id}'
            )

            if ca and exam_score:

               Result.objects.update_or_create(
               student=student,
               subject=subject,
               examination=exam,
               defaults={
               'ca_score': float(ca),
               'exam_score': float(exam_score)
            }
        )

        return redirect('result_list')

    return render(
        request,
        'results/bulk_entry.html',
        {
            'classes': classes,
            'students': students,
            'subjects': subjects,
            'exams': exams,
            'selected_class': selected_class,
        }
    )
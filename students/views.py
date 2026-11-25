from django.shortcuts import render, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.shortcuts import redirect
from django.db.models import Q

def student_list(request):

    query = request.GET.get('q')

    students = Student.objects.all()

    if query:
        students = students.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(admission_number__icontains=query)
        )

    return render(
        request,
        'students/list.html',
        {
            'students': students
        }
    )


def student_detail(request, pk):

    student = get_object_or_404(
        Student,
        pk=pk
    )

    return render(
        request,
        'students/detail.html',
        {
            'student': student
        }
    )

def student_create(request):

    if request.method == 'POST':

        form = StudentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect(
                'student_list'
            )

    else:

        form = StudentForm()

    return render(
        request,
        'students/form.html',
        {
            'form': form
        }
    )


def student_update(request, pk):

    student = get_object_or_404(
        Student,
        pk=pk
    )

    if request.method == 'POST':

        form = StudentForm(
            request.POST,
            request.FILES,
            instance=student
        )

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:

        form = StudentForm(
            instance=student
        )

    return render(
        request,
        'students/form.html',
        {
            'form': form
        }
    )

def student_delete(request, pk):

    student = get_object_or_404(
        Student,
        pk=pk
    )

    if request.method == 'POST':

        student.delete()

        return redirect(
            'student_list'
        )

    return render(
        request,
        'students/delete.html',
        {
            'student': student
        }
    )

def student_update(request, pk):

    student = get_object_or_404(
        Student,
        pk=pk
    )

    if request.method == "POST":

        form = StudentForm(
            request.POST,
            request.FILES,
            instance=student
        )

        if form.is_valid():
            form.save()
            return redirect(
                'student_detail',
                pk=student.pk
            )

    else:

        form = StudentForm(
            instance=student
        )

    return render(
        request,
        'students/form.html',
        {
            'form': form
        }
    )
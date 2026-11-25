from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from students.models import Student
from academics.models import AcademicSession, Term , ClassRoom
from .models import FeeStructure, Payment 
from .forms import PaymentForm , FeeStructureForm
from django.shortcuts import redirect
from openpyxl import Workbook
from django.http import HttpResponse


def fee_statement(request, student_id):

    student = get_object_or_404(
        Student,
        id=student_id
    )

    current_session = AcademicSession.objects.first()

    current_term = Term.objects.first()

    fee = FeeStructure.objects.filter(
        classroom=student.classroom,
        session=current_session,
        term=current_term
    ).first()

    total_fee = fee.amount if fee else 0

    amount_paid = Payment.objects.filter(
        student=student,
        session=current_session,
        term=current_term
    ).aggregate(
        Sum('amount_paid')
    )['amount_paid__sum'] or 0

    payments = Payment.objects.filter(
    student=student
    ).order_by('-payment_date')
    
    balance = total_fee - amount_paid

    if balance <= 0 and total_fee > 0:
        status = "PAID"

    elif amount_paid > 0:
        status = "PARTLY PAID"

    else:
        status = "UNPAID"

    context = {
        'student': student,
        'session': current_session,
        'term': current_term,
        'total_fee': total_fee,
        'amount_paid': amount_paid,
        'balance': balance,
        'status': status,
        'payments': payments,
    }

    return render(
        request,
        'finance/statement.html',
        context
    )


def finance_dashboard(request):

    current_session = AcademicSession.objects.first()

    current_term = Term.objects.first()

    total_expected = 0

    students = Student.objects.all()

    for student in students:

        fee = FeeStructure.objects.filter(
            classroom=student.classroom,
            session=current_session,
            term=current_term
        ).first()

        if fee:

            total_expected += fee.amount

    total_collected = Payment.objects.filter(
        session=current_session,
        term=current_term
    ).aggregate(
        Sum('amount_paid')
    )['amount_paid__sum'] or 0

    outstanding_balance = (
        total_expected -
        total_collected
    )

    context = {

        'session': current_session,

        'term': current_term,

        'total_expected': total_expected,

        'total_collected': total_collected,

        'outstanding_balance': outstanding_balance,

    }

    return render(
        request,
        'finance/dashboard.html',
        context
    )

def payment_receipt(request, payment_id):

    payment = get_object_or_404(
        Payment,
        id=payment_id
    )

    context = {
        'payment': payment
    }

    return render(
        request,
        'finance/receipt.html',
        context
    )

def debtors_list(request):

    current_session = AcademicSession.objects.first()

    current_term = Term.objects.first()

    debtors = []

    students = Student.objects.all()

    for student in students:

        fee = FeeStructure.objects.filter(
            classroom=student.classroom,
            session=current_session,
            term=current_term
        ).first()

    total_fee = fee.amount if fee else 0

    amount_paid = Payment.objects.filter(
            student=student,
            session=current_session,
            term=current_term
        ).aggregate(
            Sum('amount_paid')
        )['amount_paid__sum'] or 0

    balance = total_fee - amount_paid

    if balance > 0:

        debtors.append({

                'student': student,

                'total_fee': total_fee,

                'amount_paid': amount_paid,

                'balance': balance,

            })

    return render(
        request,
        'finance/debtors.html',
        {
            'debtors': debtors,
            'session': current_session,
            'term': current_term,
        }
    )

def payment_create(request):

    if request.method == 'POST':

        form = PaymentForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                'finance_dashboard'
            )

    else:

        form = PaymentForm()

    return render(
        request,
        'finance/payment_form.html',
        {
            'form': form
        }
    )

def export_payments_excel(request):

    workbook = Workbook()

    worksheet = workbook.active

    worksheet.title = "Payments"

    headers = [

        'Student',
        'Session',
        'Term',
        'Amount Paid',
        'Reference',
        'Payment Date',

    ]

    worksheet.append(headers)

    payments = Payment.objects.all()

    for payment in payments:

        worksheet.append([

            str(payment.student),

            str(payment.session),

            str(payment.term),

            float(payment.amount_paid),

            payment.reference,

            str(payment.payment_date),

        ])

    response = HttpResponse(

        content_type=
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

    )

    response[
        'Content-Disposition'
    ] = 'attachment; filename=payments.xlsx'

    workbook.save(response)

    return response

def class_fee_view(request):

    classes = ClassRoom.objects.all()

    selected_class = None
    fee_structure = None

    class_id = request.GET.get('class')

    if class_id:

        selected_class = ClassRoom.objects.get(
            id=class_id
        )

        fee_structure = FeeStructure.objects.filter(
            classroom=selected_class
        ).first()

    return render(
        request,
        'finance/class_fees.html',
        {
            'classes': classes,
            'selected_class': selected_class,
            'fee_structure': fee_structure,
        }
    )

def class_fee_management(request):

    fees = FeeStructure.objects.all().order_by(
        'classroom'
    )

    return render(
        request,
        'finance/class_fee_management.html',
        {
            'fees': fees
        }
    )

def fee_create(request):

    if request.method == "POST":

        form = FeeStructureForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                'class_fee_management'
            )

    else:

        form = FeeStructureForm()

    return render(
        request,
        'finance/fee_form.html',
        {
            'form': form
        }
    )

def fee_update(request, pk):

    fee = FeeStructure.objects.get(
        pk=pk
    )

    if request.method == "POST":

        form = FeeStructureForm(
            request.POST,
            instance=fee
        )

        if form.is_valid():

            form.save()

            return redirect(
                'class_fee_management'
            )

    else:

        form = FeeStructureForm(
            instance=fee
        )

    return render(
        request,
        'finance/fee_form.html',
        {
            'form': form
        }
    )

def fee_delete(request, pk):

    fee = FeeStructure.objects.get(
        pk=pk
    )

    fee.delete()

    return redirect(
        'class_fee_management'
    )
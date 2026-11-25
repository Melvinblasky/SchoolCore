from django.urls import path
from .views import (
    debtors_list,
    finance_dashboard,
    fee_statement,
    payment_receipt,
    export_payments_excel,
    class_fee_view,
    class_fee_management,
    fee_create,
    fee_delete,
    fee_update,
    payment_create
)

urlpatterns = [

    path(
        '',
        finance_dashboard,
        name='finance_dashboard'
    ),

    path(
        'statement/<int:student_id>/',
        fee_statement,
        name='fee_statement'
    ),

    path(
    'receipt/<int:payment_id>/',
    payment_receipt,
    name='payment_receipt'
    ),

    path(
    'debtors/',
    debtors_list,
    name='debtors_list'
    ),

    path(
    'payment/add/',
    payment_create,
    name='payment_create'
    ),   

    path(
    'export/payments/',
    export_payments_excel,
    name='export_payments_excel'
    ),

    path(
    'class-fees/',
    class_fee_view,
    name='class_fee_view'
    ),

    path(
    'class-fees/manage/',
    class_fee_management,
    name='class_fee_management'
    ),

    path(
        'class-fees/add/',
        fee_create,
        name='fee_create'
    ),

    path(
        'class-fees/edit/<int:pk>/',
        fee_update,
        name='fee_update'
    ),

    path(
        'class-fees/delete/<int:pk>/',
        fee_delete,
        name='fee_delete'
    ), 
]
from django.urls import path

from .views import (
    bulk_result_entry,
    report_card,
    result_list,
    result_create
)

urlpatterns = [

    path(
        '',
        result_list,
        name='result_list'
    ),

    path(
        'add/',
        result_create,
        name='result_create'
    ),

    path(
    'report-card/<int:student_id>/',
    report_card,
    name='report_card'
  
    ),

    path(
    'bulk-entry/',
    bulk_result_entry,
    name='bulk_result_entry'
),

]
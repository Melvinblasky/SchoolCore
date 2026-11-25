from django.urls import path

from .views import (
    student_create,
    student_list,
    student_detail,
    student_update,
    student_delete,
)

urlpatterns = [

    path(
        '',
        student_list,
        name='student_list'
    ),

    path(
    'add/',
    student_create,
    name='student_create'
),

    path(
    '<int:pk>/edit/',
    student_update,
    name='student_update'
),
    path(
        '<int:pk>/',
        student_detail,
        name='student_detail'
    ),

    path(
    '<int:pk>/delete/',
    student_delete,
    name='student_delete'
),

]
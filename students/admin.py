from django.contrib import admin
from .models import Student, Parent


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        'admission_number',
        'first_name',
        'last_name',
        'classroom'
    )

    search_fields = (
        'admission_number',
        'first_name',
        'last_name'
    )


admin.site.register(Parent)
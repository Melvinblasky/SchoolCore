from django.contrib import admin
from .models import (
    AcademicSession,
    Term,
    ClassRoom,
    Subject
)


admin.site.register(AcademicSession)
admin.site.register(Term)
admin.site.register(ClassRoom)
admin.site.register(Subject)
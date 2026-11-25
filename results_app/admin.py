from django.contrib import admin
from .models import Examination, Result
from .models import (
    Examination,
    Result,
    ReportCard
)

admin.site.register(ReportCard)

admin.site.register(Examination)
admin.site.register(Result)

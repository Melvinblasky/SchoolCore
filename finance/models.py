from django.db import models
from students.models import Student
from academics.models import AcademicSession, ClassRoom, Term
import uuid


class FeeStructure(models.Model):

    classroom = models.ForeignKey(
        ClassRoom,
        on_delete=models.CASCADE
    )

    session = models.ForeignKey(
        AcademicSession,
        on_delete=models.CASCADE
    )

    term = models.ForeignKey(
        Term,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):

        return (
            f"{self.classroom} - "
            f"{self.session} - "
            f"{self.term}"
        )

class Payment(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    session = models.ForeignKey(
        AcademicSession,
        on_delete=models.CASCADE
    )

    term = models.ForeignKey(
        Term,
        on_delete=models.CASCADE
    )

    amount_paid = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_date = models.DateField()

    reference = models.CharField(
        max_length=100,
        unique=True,
        blank=True
    )

    def __str__(self):
        return f"{self.student} - {self.session} - {self.term}"


def save(self, *args, **kwargs):

    if not self.reference:

        self.reference = str(
            uuid.uuid4()
        )[:8].upper()

    super().save(*args, **kwargs)
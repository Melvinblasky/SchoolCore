from django.db import models
from students.models import Student
from academics.models import Subject


class Examination(models.Model):

    name = models.CharField(
        max_length=100
    )

    session = models.CharField(
        max_length=50
    )

    term = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.name


class Result(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )

    examination = models.ForeignKey(
        Examination,
        on_delete=models.CASCADE
    )

    ca_score = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    exam_score = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    total_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True
    )

    grade = models.CharField(
        max_length=2,
        blank=True
    )

    remark = models.CharField(
        max_length=30,
        blank=True
    )

    teacher_comment = models.TextField(
    blank=True,
    null=True
)

    principal_comment = models.TextField(
    blank=True,
    null=True
)

    def save(self, *args, **kwargs):

        self.total_score = (
            float(self.ca_score) +
            float(self.exam_score)
        )

        if self.total_score >= 70:
            self.grade = "A"
            self.remark = "Excellent"

        elif self.total_score >= 60:
            self.grade = "B"
            self.remark = "Very Good"

        elif self.total_score >= 50:
            self.grade = "C"
            self.remark = "Good"

        elif self.total_score >= 45:
            self.grade = "D"
            self.remark = "Fair"

        elif self.total_score >= 40:
            self.grade = "E"
            self.remark = "Pass"

        else:
            self.grade = "F"
            self.remark = "Fail"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student} - {self.subject}"


class ReportCard(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    examination = models.ForeignKey(
        Examination,
        on_delete=models.CASCADE
    )

    teacher_comment = models.TextField()

    principal_comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.student} - {self.examination}"

class Meta:
    constraints = [
        models.UniqueConstraint(
            fields=[
                'student',
                'subject',
                'examination'
            ],
            name='unique_student_subject_exam'
        )
    ]
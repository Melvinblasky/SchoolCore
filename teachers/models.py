from django.db import models
from academics.models import Subject, ClassRoom


class Teacher(models.Model):

    employee_id = models.CharField(
        max_length=20,
        unique=True
    )

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    email = models.EmailField(
        unique=True
    )

    phone = models.CharField(
        max_length=20
    )

    subject = models.ManyToManyField(
        Subject
    )

    classes = models.ManyToManyField(
        ClassRoom
    )

    date_employed = models.DateField()

    passport = models.ImageField(
        upload_to='teachers/',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
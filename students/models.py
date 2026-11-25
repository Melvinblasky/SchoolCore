from django.db import models
from academics.models import ClassRoom
from django.utils import timezone


class Student(models.Model):

    GENDER_CHOICES = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    )

    admission_number = models.CharField(
        max_length=20,
        unique=True
    )

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    other_name = models.CharField(
        max_length=100,
        blank=True
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    date_of_birth = models.DateField()

    classroom = models.ForeignKey(
        ClassRoom,
        on_delete=models.SET_NULL,
        null=True
    )

    passport = models.ImageField(
        upload_to='students/',
        blank=True,
        null=True
    )

    address = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Parent(models.Model):

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    phone = models.CharField(max_length=20)

    email = models.EmailField(
        blank=True
    )

    occupation = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

parent = models.ForeignKey(
    Parent,
    on_delete=models.SET_NULL,
    null=True,
    blank=True
)

def save(self, *args, **kwargs):

    if not self.admission_number:

        year = timezone.now().year

        last_student = Student.objects.count() + 1
        self.admission_number = f"SCH{year}{last_student:03d}"

    super().save(*args, **kwargs)
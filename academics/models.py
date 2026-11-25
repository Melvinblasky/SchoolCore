from django.db import models

# Create your models here.

class AcademicSession(models.Model):
    name = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Term(models.Model):
    TERM_CHOICES = (
        ('FIRST', 'First Term'),
        ('SECOND', 'Second Term'),
        ('THIRD', 'Third Term'),
    )

    name = models.CharField(
        max_length=20,
        choices=TERM_CHOICES
    )

    session = models.ForeignKey(
        AcademicSession,
        on_delete=models.CASCADE
    )

    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.get_name_display()} - {self.session}"


class ClassRoom(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.name
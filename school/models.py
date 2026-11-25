from django.db import models


class School(models.Model):

    name = models.CharField(
        max_length=200
    )

    address = models.TextField()

    phone = models.CharField(
        max_length=20
    )

    email = models.EmailField()

    logo = models.ImageField(
        upload_to='school_logo/'
    )

    def __str__(self):
        return self.name
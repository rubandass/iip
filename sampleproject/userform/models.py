from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
# Create your models here.


class Request(models.Model):
    user = models.ForeignKey(
        User, related_name="participants", on_delete=models.CASCADE)
    server = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=50)
    contact_number = models.PositiveIntegerField(
        validators=[MaxValueValidator(9999999999)])
    date = models.DateTimeField()
    status = models.CharField(max_length=50)

    # class Meta:
    #     unique_together = (("user",),)

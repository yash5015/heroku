from email import message
from sre_constants import BRANCH
from statistics import mode
from django.db import models
from django.core import validators
import datetime
# Create your models here.
BRANCH_CHOICES = (
    ("Ambala", "Ambala"),
    ("Amritsar", "Amritsar"),
    ("Ajmerigate", "Ajmerigate"),
    ("Firozepur", "Firozepur"),
    ("Ghaziabad", "Ghaziabad"),
    ("Jagadhari", "Jagadhari"),
    ("Ludhiana", "Ludhiana"),
    ("Patiala", "Patiala"),
    ("Pathankot", "Pathankot"),
    ("Tuglakabad ", "Tuglakabad"),
    ("Head Qtrs.", "Head Qtrs."),
)

class Branch(models.Model):
    bname = models.CharField(max_length=100, choices=BRANCH_CHOICES, blank=False)
    bfiles = models.FileField(upload_to="", blank=False)

    def __str__(self):
        return self.bname




class Loanform(models.Model):
    name = models.CharField(max_length=100, blank=False)
    phno = models.CharField(
        validators=[validators.MinLengthValidator(10)], max_length=11, blank=False)
    regno = models.CharField(max_length=25, blank=False)
    selbranch=models.CharField(max_length=50,blank=False,choices=BRANCH_CHOICES)
    userform = models.FileField(upload_to="", blank=False)
    date = models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.regno

class Contact(models.Model):
    name=models.CharField(max_length=50)
    phno=models.CharField(max_length=11)
    message=models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Chairman_message(models.Model):
    message=models.CharField(max_length=500)

    def __str__(self):
        return self.message
    
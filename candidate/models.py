
import _datetime
from django.db import models


STATUS = (
    ("ACCEPTED", "Accepted"),
    ("REJECTED", "Rejected"),
    ("ON ASSIGNMENT", "On Hold"),
)

# Create your models here.
class Candidate(models.Model):
    Name = models.CharField(max_length=40)
    Contact = models.IntegerField()
    Email = models.EmailField(max_length=40)
    Country = models.CharField(max_length=20)
    Degree = models.CharField(max_length=40)
    Position = models.CharField(max_length=50)
    Experience = models.CharField(max_length=40)
    Resume = models.FileField(upload_to='static/resume/' , blank=True )
    Applied_for = models.CharField(max_length=40)
    Applied_on = models.DateTimeField(default=_datetime.date.today())
    Status = models.CharField(
        max_length = 15,
        choices = STATUS,
        default = 'Hold'
        )
    Skills = models.TextField(unique=True)

    def __str__(self):
        return self.Name
    




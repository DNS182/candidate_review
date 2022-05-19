from datetime import datetime
from django.db import models


STATUS = (
    ("ACCEPTED", "Accepted"),
    ("REJECTED", "Rejected"),
    ("ON ASSIGNMENT", "On Hold"),
)

# Create your models here.
class Candidate(models.Model):
    Name = models.CharField(max_length=40)
    Contact = models.IntegerField(unique=True)
    Email = models.EmailField(max_length=40 , unique= True)
    Address = models.CharField(max_length=100)
    Degree = models.CharField(max_length=40)
    Position = models.CharField(max_length=50)
    Experience = models.CharField(max_length=40)
    Resume = models.FileField(upload_to='static/resume/' , blank=True )
    Applied_for = models.CharField(max_length=40)
    Applied_on = models.DateTimeField(default= datetime.now())
    Status = models.CharField(
        max_length = 15,
        choices = STATUS,
        default = 'ON ASSIGNMENT'
        )
    Skills = models.TextField(default='relax')

    def __str__(self):
        return self.Name
    




from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    job_title=models.CharField(max_length=100)
    description=models.TextField()
    salary_range=models.CharField(max_length=50,blank=True)
    posted_on=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    company=models.CharField(max_length=50)
    location=models.CharField(max_length=30)

class Application(models.Model):
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    applicant=models.ForeignKey(User,on_delete=models.CASCADE)
    STATUS_CHOICE=(
        ('pending','Pending'),
        ('rejected','Rejected'),
        ('shortlisted','Shortlisted'),
        ('hired','Hired')
    )
    status=models.CharField(choices=STATUS_CHOICE,max_length=20,default='pending')
    applied_on=models.DateTimeField(auto_now_add=True)
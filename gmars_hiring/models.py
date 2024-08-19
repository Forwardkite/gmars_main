from django.db import models

# Create your models here.

class Job(models.Model):
    job_title = models.CharField(max_length=20)
    job_industry = models.CharField(max_length=20)
    job_country = models.CharField(max_length=20)
    job_description = models.TextField()

    def __str__(self):
        return self.job_title

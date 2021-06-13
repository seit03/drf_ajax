from django.db import models


class Job(models.Model):
    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
    JOB_TYPES = [('remote', '1'), ('office', '2')]
    job_types = models.CharField(max_length=50, choices=JOB_TYPES,
                                 default='office')
    posted_on = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=90)

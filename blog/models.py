# core django
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.
class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampModel):
    DRAFT = 'dr'
    STAGING = 'st'
    PUBLISHED = 'pu'
    status_choices = (
        (DRAFT, 'Draft'),
        (STAGING, 'Staging'),
        (PUBLISHED, 'Published')
    )

    author = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE)

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(default=now)
    status = models.CharField(
        max_length=2, choices=status_choices, default=DRAFT)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-publish',)

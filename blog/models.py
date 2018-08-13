# core django
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.shortcuts import reverse


# third party
from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices
from taggit.managers import TaggableManager


# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status=Post.STATUS.published)


class Post(TimeStampedModel, StatusModel):

    author = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE)

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(default=now)
    objects = models.Manager()
    STATUS = Choices('draft', 'staging', 'published')
    published = PublishedManager()
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-publish',)

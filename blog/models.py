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


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status=Post.PUBLISHED)


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
    objects = models.Manager()
    published = PublishedManager()
    status = models.CharField(
        max_length=2, choices=status_choices, default=DRAFT)

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

from django.contrib.postgres.fields import JSONField
from django.db import models

from user.models import User


def upload_image_to(instance, filename):
    return 'posts/%s' % (
        instance.id
    )

class Post(models.Model):
    caption = models.TextField()
    image = models.ImageField(upload_to=upload_image_to, null=True, blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(blank=True, max_length=120)
    tags = JSONField(null=True, blank=True) # <---- Use ArrayField instead!
    posted_by = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    comment = models.TextField()
    commented_at = models.DateTimeField(auto_now_add=True)
    commented_by = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
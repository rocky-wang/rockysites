# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

class Door(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        error_messages={
        'unique': 'That identifier name is already saved.'
        }
    )

    antipassback = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.name

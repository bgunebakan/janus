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
    health = models.BooleanField(default=True)
    identifier_type = models.ForeignKey('identifiers.Identifier_types')
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)


from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

class Permission(models.Model):
    identifier = models.ForeignKey('identifiers.Identifier_types')
    door = models.ForeignKey('doors.door')
    permission = models.ForeignKey('Permission_types')
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)


class Permission_types(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        error_messages={
        'unique': 'That identifier type is already saved.'
        }
    )
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

 

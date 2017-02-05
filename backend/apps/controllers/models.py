from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

class Controller(models.Model):
    mac = models.CharField(
        max_length=12,
        unique=True,
        error_messages={
        'unique': 'That identifier mac is already saved.'
        }
    )
    ip_address = models.GenericIPAddressField(unique=True)
    direction = models.BooleanField()
    health = models.BooleanField(default=True)
    identifier_type = models.ForeignKey('identifiers.Identifier_types')
    door = models.ForeignKey('doors.Door')
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.mac

from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

class Permission(models.Model):
    identifier = models.ForeignKey('identifiers.Identifier')
    door = models.ForeignKey('doors.door')
    permission = models.ForeignKey('Permission_types')
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return 'Door: '+ self.door.name + ' Identifier: '+ self.identifier.key

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

    def __unicode__(self):
        return self.name

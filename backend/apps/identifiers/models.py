from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

class Identifier(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        error_messages={
        'unique': 'That identifier name is already saved.'
        }
    )
    key = models.CharField(
        max_length=255,
        unique=True,
        error_messages={
        'unique': 'That identifier is already saved.'
        }
    )
    is_active = models.BooleanField(default=False)
    identifier_type = models.ForeignKey('Identifier_types', on_delete=models.CASCADE)
    user = models.ForeignKey('users.EmailUser')
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)
   
    def __unicode__(self):
        return self.key

class Identifier_types(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        error_messages={
        'unique': 'That identifier type is already saved.'
        }
    )
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

   

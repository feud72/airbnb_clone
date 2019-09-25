from django.db import models


class TimeStampedModel(models.Model):

    """ Tiem Stamped Model """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        abstract = True

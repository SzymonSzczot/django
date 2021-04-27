from django.db import models


class Event(models.Model):

    name = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=1000, default="")
    due_date = models.DateTimeField(blank=True)
    created = models.DateTimeField(auto_created=True)

    class Meta:
        pass

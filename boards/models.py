from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=100, default="")

    class Meta:
        pass

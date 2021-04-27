from django.db import models


class BaseFile(models.Model):

    name = models.CharField(max_length=100)


class PackageShort(models.Model):

    url = models.CharField(max_length=100, default="", unique=True)
    name = models.CharField(max_length=50, default="")
    version = models.CharField(max_length=20, default="")
    description = models.CharField(max_length=300, default="")
    hosted = models.DateTimeField(null=True)
    origin_file = models.ForeignKey(
        "search_engine.BaseFile",
        on_delete=models.DO_NOTHING,
        related_name="shorts"
    )

    package = models.OneToOneField(
        "search_engine.Package",
        on_delete=models.SET_NULL,
        related_name="short",
        null=True
    )


class Package(models.Model):

    description = models.CharField(max_length=4000, default="")
    stars = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Package"

import re
from os import listdir

from dateutil import parser
from django.core.management.base import BaseCommand

from search_engine.models import PackageShort, BaseFile


class Command(BaseCommand):

    def handle(self, *args, **options):
        files = [f for f in listdir("data\\shorts")]

        for file in files:
            base_file = BaseFile.objects.create(name=file)
            packages = []
            print(file)
            with open(f"data\\clean_shorts\\{file}", "r", encoding="utf-8") as file_to_save:
                for line in file_to_save.readlines():
                    print(line.split(", "))
                    *rest, hosted = line.split(", ")
                    try:
                        url, name, version, *dsc = rest
                    except ValueError:
                        dsc = rest
                    description = ", ".join(dsc)
                    try:
                        parser.parse(hosted)
                        hosted = hosted.strip("\n").strip(" ")
                    except:
                        hosted = None
                    packages.append(
                        PackageShort(
                            url=url,
                            name=name,
                            version=version,
                            description=description,
                            hosted=hosted,
                            origin_file=base_file
                        )
                    )
                PackageShort.objects.bulk_create(packages, ignore_conflicts=True)

from django.core.management import BaseCommand

from search_engine.models import PackageShort


class Command(BaseCommand):

    def handle(self, *args, **options):
        PackageShort.objects.all().delete()
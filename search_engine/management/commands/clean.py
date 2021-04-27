import re
from os import listdir

from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        files = [f for f in listdir("data\\shorts")]

        for file in files[:1]:
            with open(f"data\\clean_shorts\\{file}", "w", encoding="utf-8") as file_to_save:
                with open(f"data\\shorts\\{file}", "r", encoding="utf-8") as file_to_clean:
                    text = str(file_to_clean.read())
                    new_file = re.sub("\n(?!/)", " ", text)
                    file_to_save.write(new_file)

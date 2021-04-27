from django.core.management import BaseCommand

from search_engine.models import PackageShort


class Command(BaseCommand):

    def handle(self, *args, **options):
        from elasticsearch_dsl import analyzer, tokenizer

        my_analyzer = analyzer('my_analyzer',
                               tokenizer=tokenizer("standard"),
                               filter=["stop"]
                               )

        response = my_analyzer.simulate('Hello World! Is something wrong with you? I want to ask. manager')

        # ['hel', 'ell', 'llo', 'lo ', 'o w', ' wo', 'wor', 'orl', 'rld', 'ld!']
        tokens = [t.token for t in response.tokens]
        print(tokens)
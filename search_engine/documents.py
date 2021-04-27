# documents.py

from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl import analyzer, tokenizer

from search_engine.models import PackageShort, Package
from django.conf import settings
from django_elasticsearch_dsl import Index, fields
from elasticsearch_dsl import analyzer

INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])

# See Elasticsearch Indices API reference for available settings
INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)

html_strip = analyzer(
    'html_strip',
    tokenizer=tokenizer('trigram', 'nGram', min_gram=3, max_gram=3),
    filter=["standard", "lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)


@INDEX.doc_type
class CarDocument(Document):
    """Book Elasticsearch document."""

    id = fields.IntegerField(attr='id')

    name = fields.TextField(
        attr="name",
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )

    description = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
            'tokenized': fields.TextField(analyzer=html_strip),
        }
    )

    hosted = fields.DateField(
        fields={
            "raw": fields.DateField()
        }
    )

    version = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )

    url = fields.TextField(attr="url")

    class Django(object):
        """Meta options."""
        model = PackageShort

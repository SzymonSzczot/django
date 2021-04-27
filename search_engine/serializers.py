from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from search_engine.documents import CarDocument


class CarDocumentSerializer(DocumentSerializer):
    class Meta:
        document = CarDocument
        fields = (
            'id',
            'name',
            "description",
            "url",
            "hosted",
            "version"
        )

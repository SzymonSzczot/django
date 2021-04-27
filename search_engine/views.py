
from django.http import HttpResponse
from django.template import loader
from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_TERMS,
    LOOKUP_FILTER_RANGE,
    LOOKUP_FILTER_PREFIX,
    LOOKUP_FILTER_WILDCARD,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
    LOOKUP_QUERY_EXCLUDE,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    IdsFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    SearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination
from rest_framework import views
from rest_framework.response import Response

from search_engine.documents import CarDocument
from search_engine.serializers import CarDocumentSerializer


class BookDocumentView(BaseDocumentViewSet):
    """The BookDocument view."""

    document = CarDocument
    serializer_class = CarDocumentSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]
    # Define search fields
    search_fields = (
        'url',
        "description",
        "name"
    )
    # Define filter fields
    filter_fields = {
        'id': {
            'field': 'id',
            # Note, that we limit the lookups of id field in this example,
            # to `range`, `in`, `gt`, `gte`, `lt` and `lte` filters.
            'lookups': [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_GT,
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
            ],
        },
        'url': {
            'field': 'url',
            'lookups': [
                LOOKUP_FILTER_TERMS,
                LOOKUP_FILTER_PREFIX,
                LOOKUP_FILTER_WILDCARD,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_EXCLUDE,
            ],
        },
        "name": "name",
        'description': {
            'field': 'description.tokenized',
            # Note, that we limit the lookups of `tags` field in
            # this example, to `terms, `prefix`, `wildcard`, `in` and
            # `exclude` filters.
            'lookups': [
                LOOKUP_FILTER_TERMS,
                LOOKUP_FILTER_PREFIX,
                LOOKUP_FILTER_WILDCARD,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_EXCLUDE,
            ],
        },
        "hosted": "hosted.raw",
    }
    # Define ordering fields
    ordering_fields = {
        'id': 'id',
        "hosted": "hosted.raw"
    }
    # Specify default ordering
    ordering = ('id',)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        template = loader.get_template('search.html')
        context = {
            'search': response.data["results"],
        }
        return HttpResponse(template.render(context, request))


class Test(views.APIView):
    permission_classes = ()
    def get(self, request, **kwargs):
        xddd = CarDocument.search().query("match", description="Biology")
        for d in xddd:
            print(d)
        import pdb;pdb.set_trace()
        return Response()

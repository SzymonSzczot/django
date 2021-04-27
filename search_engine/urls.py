from django.conf.urls import url
from rest_framework import routers
from django.urls import path, include

from search_engine.views import BookDocumentView, Test

router = routers.SimpleRouter()
router.register("items", BookDocumentView, basename="items")

urlpatterns = [
    url(r'^', include(router.urls)),
    url("test", Test),
]

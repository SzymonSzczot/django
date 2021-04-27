from django.urls import path
from rest_framework import routers

from .views import EventView

router = routers.SimpleRouter()
router.register("items", EventView, basename="items")

urlpatterns = []
urlpatterns += router.urls

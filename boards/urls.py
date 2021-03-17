from django.urls import path
from rest_framework import routers

from .views import BoardView

router = routers.SimpleRouter()
router.register("items", BoardView, basename="items")

urlpatterns = []
urlpatterns += router.urls

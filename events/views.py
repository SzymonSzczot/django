from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from rest_framework import viewsets

from events.serializers import EventSerializer
from .models import Event


class EventView(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import BoardSerializer
from .models import Board


class BoardView(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()

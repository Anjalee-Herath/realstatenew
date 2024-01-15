from django.shortcuts import render
from rest_framework import viewsets
from .models import Property
from .serializers import PropertySerializer

class PropertyView(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

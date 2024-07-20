from django.shortcuts import render
from rest_framework import viewsets
from .models import MenuItem,FeatureBlock
from .serializers import FeatureBlockSerializer,MenuItemSerializer

class MenuItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class FeatureBlockViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FeatureBlock.objects.all()
    serializer_class = FeatureBlockSerializer

from rest_framework import serializers
from .models import MenuItem, FeatureBlock

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'url', 'order']

class FeatureBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureBlock
        fields = ['id', 'description', 'order']

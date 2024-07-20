# backend/admin.py
from django.contrib import admin
from .models import MenuItem, FeatureBlock 

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'order')

@admin.register(FeatureBlock)
class FeatureBlockAdmin(admin.ModelAdmin):
    list_display = ('description', 'order')  

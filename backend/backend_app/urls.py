from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet,FeatureBlockViewSet

router = DefaultRouter()
router.register(r'menu-items', MenuItemViewSet)
router.register(r'feature-blocks', FeatureBlockViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

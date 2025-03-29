from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'', ProductViewSet, basename='products')

urlpatterns = router.urls
from django.urls import include, path
from .viewsets import ProductViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register("products", ProductViewSet)

urlpatterns = router.urls

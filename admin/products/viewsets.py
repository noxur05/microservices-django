from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product
from producer import publish

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        if self.action == "list":
            publish()
        return super().get_queryset()
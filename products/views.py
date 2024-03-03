from rest_framework import generics, status
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        res = super().delete(request, *args, **kwargs)
        print('aaaa', res.data)
        return Response(
            data={'status': 'deleted'},
            status=status.HTTP_204_NO_CONTENT,
        )

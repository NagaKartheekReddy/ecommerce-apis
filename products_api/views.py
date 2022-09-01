from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    # default initial data ordering on these fields
    queryset = Product.objects.order_by('price', 'vendor', 'category')
    serializer_class = ProductSerializer
    # filter options list
    filter_backends = [SearchFilter, OrderingFilter]
    # search on category field eg: /list/products/?search=hobbies
    search_fields = ['category', 'vendor', 'price']
    # provides all ordering options on these 3 fields eg:/list/products/?ordering=-price(desc order)
    ordering_fields = ['price', 'vendor', 'category']


def custom404(request, exception=None):
    return JsonResponse({
        'status_code': 404,
        'error': 'The resource was not found. Please check again'
    })

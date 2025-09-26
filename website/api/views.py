from django import http
from website.models import Products
from website.api.serialization.product_serializer import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes([AllowAny])
def product_list(request):
    print("Product list view called")
    serialized = ProductSerializer(Products.objects.all(), many=True)
    print("Serialized data:", serialized.data)  # DEBUG
    # products = Products.objects.all().values('id','product_name','product_description','price')
    # return http.JsonResponse(list(products), safe=False)
    return Response(serialized.data)
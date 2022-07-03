from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ProductCategory
from .serializers import ProductCategorySerializer



@api_view(['GET', 'POST'])
def product_category_list(request):
    """
    List all product categories, or create a new one.
    """
    if request.method == 'GET':
        snippets = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def product_category_detail(request, pk):
    """
    Retrieve, update or delete a product category.
    """
    try:
        snippet = ProductCategory.objects.get(pk=pk)
    except ProductCategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductCategorySerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductCategorySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

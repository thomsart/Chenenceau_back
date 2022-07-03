from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ProductName
from .serializers import ProductNameSerializer



@api_view(['GET', 'POST'])
def product_name_list(request):
    """
    List all product names, or create a new one.
    """
    if request.method == 'GET':
        snippets = ProductName.objects.all()
        serializer = ProductNameSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductNameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def product_name_detail(request, pk):
    """
    Retrieve, update or delete a product name.
    """
    try:
        snippet = ProductName.objects.get(pk=pk)
    except ProductName.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductNameSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductNameSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

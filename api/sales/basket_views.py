from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import User
from .models import Basket, Product
from .serializers import BasketSerializer



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def basket_list(request, user_id):
    """
    List all products contains in the basket, or add a new product in it.
    """
    # a mon avis il doit y avoir un moyen de chopper le user autrement
    user = User.objects.get(id=user_id)
    if request.method == 'GET':
        basket = Basket.objects.filter(user=user)
        serializer = BasketSerializer(basket, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BasketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def basket_detail(request, pk):
#     """
#     Retrieve, update or delete a Basket.
#     """
#     try:
#         Basket = Basket.objects.get(pk=pk)
#     except Basket.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = BasketSerializer(Basket)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = BasketSerializer(Basket, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         Basket.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
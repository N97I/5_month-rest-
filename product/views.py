from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category, Review
from .serializers import (
    CategorySerializer, 
    ProductSerializer, 
    ReviewSerializer, 
    CategoryDetailSerializer, 
    ProductDetailSerializer, 
    ReviewDetailSerializer,
)

@api_view(http_method_names=['GET'])
def category_list_api_view(request):

    categories = Category.objects.all()
    data = CategorySerializer(instance=categories, many=True).data
    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        categorie = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = CategoryDetailSerializer(categorie, many=False).data
    return Response(data=data)

@api_view(http_method_names=['GET'])
def product_list_api_view(request):

    products = Product.objects.all()
    data = ProductSerializer(instance=products, many=True).data
    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = ProductDetailSerializer(product, many=False).data
    return Response(data=data)


@api_view(http_method_names=['GET'])
def review_list_api_view(request):

    reviews = Review.objects.all()
    data = ReviewSerializer(instance=reviews, many=True).data
    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = ReviewDetailSerializer(review, many=False).data
    return Response(data=data)
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
    ProductReviewSerializer
)

@api_view(http_method_names=['GET', 'POST'])
def category_list_create_api_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        data = CategorySerializer(instance=categories, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        name = request.data.get('name')

        product = Category.objects.create(
            name=name
        )
        return Response(status=status.HTTP_201_CREATED,
                        data=CategorySerializer(product).data)

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request, id):
    try:
        categories = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':   
        data = CategoryDetailSerializer(categories, many=False).data
        return Response(data=data)
    if request.method == 'PUT':
        categories.name = request.data.get('name')
        categories.save()
        return Response(status=status.HTTP_201_CREATED,data=CategoryDetailSerializer(categories).data)
    if request.method == 'DELETE':
        categories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(http_method_names=['GET', 'POST'])
def product_list_create_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data = ProductSerializer(instance=products, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        category_id = request.data.get('category_id')


        product = Product.objects.create(
            title=title,
            description=description,
            price=price,
            category_id=category_id,

        )
        return Response(status=status.HTTP_201_CREATED,
                    data=ProductSerializer(product).data)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        data = ProductDetailSerializer(product, many=False).data
        return Response(data=data)
    
    elif request.method == 'PUT':
        product.title = request.data.get('title')
        product.description = request.data.get('description')
        product.price = request.data.get('price')
        product.category_id = request.data.get('category_id')
        product.save()
        return Response(status=status.HTTP_201_CREATED, data=ProductDetailSerializer(product).data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(http_method_names=['GET', 'POST'])
def review_list_create_api_view(request):
    if request.method =='GET':
        reviews = Review.objects.all()
        data = ReviewSerializer(instance=reviews, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        text = request.data.get('text')
        stars = request.data.get('stars')
        product_id = request.data.get('product_id')
        rating = request.data.get('rating')

        reviews = Review.objects.create(
            text=text,
            stars=stars,
            product_id=product_id,
            rating=rating
        )
        return Response(status=status.HTTP_201_CREATED,data=ReviewSerializer(reviews).data)



@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ReviewDetailSerializer(reviews, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        reviews.text = request.data.get('text')
        reviews.stars = request.data.get('stars')
        reviews.product_id = request.data.get('product_id')
        reviews.rating = request.data.get('rating')
        reviews.save()
        return Response(status=status.HTTP_201_CREATED, data=ReviewDetailSerializer(reviews).data)
    elif request.method == 'DELETE':
        reviews.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    





@api_view(['GET'])
def product_review_list_api_view(request):
    product_review = Product.objects.all()
    data = ProductReviewSerializer(instance=product_review, many=True).data
    return Response(data, status=status.HTTP_200_OK)
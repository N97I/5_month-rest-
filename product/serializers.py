from rest_framework import serializers
from .models import Category, Product, Review
from django.db.models import Avg
from rest_framework.exceptions import ValidationError



class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = 'id', 'name', 'product_count'

    def get_product_count(self, obj):
        return obj.products.count()

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id', 'title', 'description', 'price', 'category'

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text product stars'.split()

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = 'id', 'title', 'description', 'price', 'category', 'reviews', 'average_rating'

    def get_average_rating(self, obj):
        average_rating = obj.reviews.aggregate(Avg('rating'))['rating__avg']
        return average_rating if average_rating is not None else 0
    

class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=1)


class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=3, max_length=255)
    description = serializers.CharField(required=False)
    price = serializers.IntegerField(min_value=1)
    category_id = serializers.IntegerField()

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except:
            raise ValidationError('Category does not exist!')
        return category_id
    
class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=3, max_length=255)
    stars = serializers.IntegerField(min_value=1, max_value=5)
    product_id = serializers.IntegerField()
    rating = serializers.IntegerField(min_value=1, max_value=5)

    def validate_product_id(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except:
            raise ValidationError('Product does not exist!')
        return product_id


    

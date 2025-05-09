from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.TextField(max_length=356)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.title

STARS = ((i, "*" * i) for i  in range(1,6))


class Review(models.Model):
    text = models.TextField(max_length=255)
    stars = models.IntegerField(choices=STARS, default=5)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(default=5)

    def __str__(self):
        return f'{self.text}, {self.product}'

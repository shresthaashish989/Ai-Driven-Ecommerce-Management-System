from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name=models.CharField(max_length=200 ,unique=True)
    description=models.TextField(null=True ,unique=True)

    def __str__(self):
        return self.category_name

 
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    image = models.FileField(upload_to='static/uploads', null=True)
    size = models.FloatField(default=0) 
    gender = models.CharField(max_length=10, choices=(('male','Male'),('female','Female')), default='male')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    PAYMENT_METHOD = (
        ('cash on delivery', 'cash on delivery'),
        ('esewa', 'esewa'),
        ('khalti', 'Khalti'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD, default='cash_on_delivery')
    status = models.CharField(max_length=20, default='Pending')
    address=models.CharField(max_length=100)
    contact=models.CharField(max_length=20)
    email=models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username} - {self.product.name}"
    



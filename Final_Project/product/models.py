from django.db import models

# Create your models here.

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
    



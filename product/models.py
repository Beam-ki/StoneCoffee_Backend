from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Category(models.Model):
    type=models.CharField(max_length=50)

class Product(models.Model):
    Catagory_id=models.ForeignKey(Category, on_delete=models.CASCADE,blank=True, null=True)
    content=models.TextField()
    name=models.CharField(max_length=50)
    price=models.IntegerField() 
    aroma_grade=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    sweet_grade=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    acidity_grade=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    body_grade=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    like=models.BooleanField()
    type=models.IntegerField()
    image=models.ImageField(upload_to='product_image')

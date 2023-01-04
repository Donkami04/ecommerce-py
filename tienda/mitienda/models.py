from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=45)
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name

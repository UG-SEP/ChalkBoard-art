import datetime
from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    name=models.TextField()
    def __str__(self):
        return self.name

class Food(models.Model):
    name=models.TextField()
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    is_special=models.BooleanField()
    is_popular=models.BooleanField()
    price=models.IntegerField()
    image=models.FileField(upload_to="images")
    description=models.TextField()
    def __str__(self):
        return self.name
    
class Items(models.Model):
    food=models.ForeignKey(Food,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.food.name

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=1000)
    address=models.TextField()
    phone=models.TextField()
    dish=models.ManyToManyField(Food)
    razorpay_payment_id=models.CharField(max_length=100,blank=True)
    pay_on_delivery=models.BooleanField(default=False)
    shipped=models.BooleanField(default=False)
    order_received=models.BooleanField(default=False)
    paid=models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.name +' '+ self.address
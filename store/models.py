from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='Category',null=True, blank=True)

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            pass

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Product(models.Model):
    choice = (
        ('Select a size','Select a size'),
        ('Small','Small'),
        ('Medium','Medium'),
        ('Large','Large'),
        ('Extra large','Extra large'),
    )

    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='Product')
    description = models.TextField()
    color = models.ManyToManyField(Color)
    size = models.CharField(max_length=30,choices=choice)
    quantity = models.IntegerField(default=1)
    reyting = models.FloatField(default=0)
    discount = models.FloatField(default=0)

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            pass

    def __str__(self):
        return self.name

class Card(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    total_price = models.FloatField(default=0)

    @property
    def total(self):
        self.total_price = sum([i.price*(1-i.discount/100) for i in self.product.all()])
        self.save()


    def __str__(self):
        return f"{self.user.username} | {self.total_price}"

class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return f"{self.id} | {self.user.username}"

class SaleHistory(models.Model):
    payment = (
        ('Humo', 'Humo'),
        ('UzCard', 'UzCard'),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ManyToManyField(Product)
    payment_type = models.CharField(max_length=20,choices=payment)
    total_price = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} | {self.user.username} | {self.time}"

from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Category(models.Model):
    #start class
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    #end class Category

##############################################################

class Book(models.Model):
    #Start class
    statusOption = [
        ('availble', 'availble'),
        ('rental', 'rental'),
        ('sold', 'sold'),
    ]
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, null=True, blank=True)
    photoBook = models.ImageField(upload_to='photos', null=True, blank=True)
    photoAuthor = models.ImageField(upload_to='photos', null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    rentalPriceDay = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    rentalPeriod = models.IntegerField(null=True, blank=True)
    totalRental = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=statusOption, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
    
    #end class Book

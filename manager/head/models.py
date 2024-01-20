from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=12)
    def __str__(self):
        return self.name
class Book(models.Model):
    status_book = [
        ('available', 'available'),
        ('rental', 'rental'),
        ('sold', 'sold'),

    ]
    title = models.CharField(max_length=250)
    auther = models.CharField(max_length=25)
    photo_book = models.ImageField(upload_to='photos',null=True, blank=True)
    photo_auther = models.ImageField(upload_to='photos', null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2, null=True, blank=True)
    retal_p_day = models.DecimalField(max_digits=5,decimal_places=2, null=True, blank=True)
    retal_period = models.IntegerField(null=True, blank=True)
    active= models.BooleanField(default=True)
    status = models.CharField(max_length=25, choices=status_book, null=True, blank=True)
    catagory = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.title

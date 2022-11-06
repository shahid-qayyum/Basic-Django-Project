from django.urls import reverse
from django.db import models
from django.shortcuts import reverse
from django.conf import settings
from django_countries.fields import CountryField

# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class shelter(models.Model):
    name = models.CharField(max_length=255)
    total_dog = models.IntegerField()
    total_cat = models.IntegerField()
    workers = models.IntegerField()
    city = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name
class pet(models.Model):
    breed=models.CharField(max_length=100)
    age=models.IntegerField()
    img=models.ImageField(upload_to='img/')
    category=models.ForeignKey(category, on_delete=models.CASCADE)
    shelter=models.ForeignKey(shelter, on_delete=models.CASCADE)

    def __str__(self):
        return self.breed
    
    def get_absolute_url(self):
        return reverse("petdetail", kwargs={"pk":self.pk})




class article(models.Model):
    tittle= models.CharField(max_length=255)
    intro= models.CharField(max_length=255)
    description= models.TextField()


    def __str__(self):
        return self.tittle

class contact(models.Model):
    name: models.CharField(max_length=255)
    email= models.EmailField()
    subject= models.CharField(max_length=255)
    description= models.TextField()

    def __str__(self):
        return self.email

class choice(models.Model):
    PET_CHOICES= (
        ('dog','dog'),
        ('cat','cat')
    )

    name: models.CharField(max_length=255)
    email= models.EmailField()
    pet= models.CharField(max_length=50, choices=PET_CHOICES)
    pet_breed= models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip=models.IntegerField()
    country=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)

    def __str__(self):
        return str(self.user.username)
class order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    pet=models.ForeignKey(pet, on_delete=models.CASCADE)
    address=models.ForeignKey(address, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)
    def get_absolute_url(self):
        return reverse("checkout", kwargs={"pk":self.pk})
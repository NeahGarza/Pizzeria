from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#Define structure of database (class, attributes, methods)

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images',blank=True)

    CHEESE = "C"
    HAWAIIAN = "H"
    MEATLOVERS = "M"
    PEPPERONI = "P"
    SUPREME = "S"

    PIZZA_PIC_CHOICES = [
        (CHEESE, 'Cheese'),
        (HAWAIIAN, 'Hawaiian'),
        (MEATLOVERS, 'MeatLovers'),
        (PEPPERONI, 'Pepperoni'),
        (SUPREME, 'Supreme'),
    ]

    pizza_type = models.CharField(max_length=1, choices=PIZZA_PIC_CHOICES, default=None)

    #We do this because otherwise we couln't see the output 
    def __str__(self):
        return self.name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()

    class Meta:
        #This makes the toppings plural using a pre-defined dictionary 
        # instead of just adding an s to the end of the original
        verbose_name_plural = 'toppings'

    def __str__(self):
        return self.name

class Profile(models.Model):
    first_name = models.CharField(max_length=200,blank=True)
    last_name = models.CharField(max_length=200,blank=True)
    email = models.EmailField(max_length=300,blank=True)
    dob = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username}"

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    username = models.ForeignKey(User, related_name='details', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.text
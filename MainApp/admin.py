from django.contrib import admin
from . models import Pizza, Topping, Comment, Profile

# Register your models here.

from .models import Pizza
admin.site.register(Pizza)

from .models import Topping
admin.site.register(Topping)

from .models import Comment
admin.site.register(Comment)

from .models import Profile
admin.site.register(Profile)

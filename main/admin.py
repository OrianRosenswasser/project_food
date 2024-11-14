from django.contrib import admin
from .models import Member, FoodPost, FoodRequest

# Register your models here.
admin.site.register(Member)
admin.site.register(FoodPost)
admin.site.register(FoodRequest)
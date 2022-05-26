from turtle import home
from unicodedata import category
from django.contrib import admin

from home.models import Category, Cities, Home, Publisher

# Register your models here.

admin.site.register(Home)
admin.site.register(Publisher)
admin.site.register(Category)
admin.site.register(Cities)
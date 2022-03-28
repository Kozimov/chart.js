from django.contrib import admin
from .models import Country, Post

admin.site.register(Post)
admin.site.register(Country)
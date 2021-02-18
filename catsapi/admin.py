from django.contrib import admin

# Register your models here.
from catsapi.models import User, Cat

admin.site.register(User)
admin.site.register(Cat)

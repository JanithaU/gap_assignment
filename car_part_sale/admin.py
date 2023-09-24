from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Part)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)

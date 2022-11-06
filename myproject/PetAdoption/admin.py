from django.contrib import admin
from .models import shelter,article,contact,category,pet,order,address
# Register your models here.
admin.site.register(shelter)
admin.site.register(article)
admin.site.register(category)
admin.site.register(pet)
admin.site.register(order)
admin.site.register(address)
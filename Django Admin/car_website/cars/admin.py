from django.contrib import admin
from cars.models import  Car


# Register your models here.
# admin.site.register(Car) ## --> this is the simple way to register the model to the Django Admin Interface

class CarAdmin(admin.ModelAdmin):
    # fields = ['year', 'brand']  # --> reorder the fields
    fieldsets = [    
        ('TIME INFORMATION', {'fields': ['year']}),
        ('CAR INFORMATION', {'fields': ['brand']})
    ]  # --> this way to structure the fields into groups

admin.site.register(Car, CarAdmin)

# read more here https://docs.djangoproject.com/en/4.2/ref/contrib/admin/
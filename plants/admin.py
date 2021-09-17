from django.contrib import admin
from .models import Plants
# Register your models here.




class PlantsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'price'
    )

admin.site.register(Plants, PlantsAdmin)
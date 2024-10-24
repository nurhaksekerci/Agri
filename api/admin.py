from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Farmer)
admin.site.register(Partner)
admin.site.register(Land)
admin.site.register(City)
admin.site.register(District)
admin.site.register(Neighborhood)
admin.site.register(Street)
admin.site.register(LandDetail)
admin.site.register(TodoList)
admin.site.register(WeatherAlert)
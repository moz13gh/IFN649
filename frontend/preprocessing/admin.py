from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Air_Quality_Reading)
admin.site.register(Temperature_Reading)
admin.site.register(Humidity_Reading)
admin.site.register(Peripheral)
admin.site.register(Action)


from django.contrib import admin
from .models import databook, fackey, stukey

# Register your models here.
admin.site.register(databook)
admin.site.register(fackey)
admin.site.register(stukey)
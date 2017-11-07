from django.contrib import admin

# Register your models here.
from .models import University, Org

admin.site.register(University)
admin.site.register(Org)

from django.contrib import admin

# Register your models here.

from .models import AboutUs, Members

admin.site.register(AboutUs)
admin.site.register(Members)

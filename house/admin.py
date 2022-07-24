from django.contrib import admin

from .models import House

class HouseAdmin(admin.ModelAdmin):
    readonly_fileds = ('id', 'created_on')

admin.site.register(House, HouseAdmin)
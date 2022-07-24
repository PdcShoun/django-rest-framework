from django.contrib import admin

from .models import Profile
# Register your models here.

class ProFileAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Profile, ProFileAdmin)
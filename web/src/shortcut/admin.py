from django.contrib import admin

from .models import Url

class UrlAdmin(admin.ModelAdmin):
    list_display = ('id','origin_addr', 'short_addr')

admin.site.register(Url,UrlAdmin)
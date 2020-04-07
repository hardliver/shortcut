from django.contrib import admin

from .models import Host, Url


class HostAdmin(admin.ModelAdmin):
    list_display = ('id', 'addr_code','host_addr')

class UrlAdmin(admin.ModelAdmin):
    list_display = ('id', 'host_code', 'path_code', 'web_path')

admin.site.register(Host,HostAdmin)
admin.site.register(Url,UrlAdmin)
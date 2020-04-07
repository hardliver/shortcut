from django.db import models
from django.utils.crypto import get_random_string
from django.core.cache import caches

from urllib.parse import urlparse

class Host(models.Model):
    host_addr = models.URLField(max_length=300, unique=True)
    addr_code = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return '{0}'.format(self.host_addr)
    def __unicode__(self):
        return '{0}'.format(self.host_addr)

    def save(self, *args, **kwargs):
        origin = urlparse(self.host_addr)
        self.host_addr = origin.scheme + '://' + origin.hostname
        length = 3
        addr_code = None
        while not addr_code or Host.objects.filter(addr_code=addr_code).exists():
            addr_code = get_random_string(length)
            length += 1
        self.addr_code = addr_code
        return super().save(*args, **kwargs)


class Url(models.Model):
    web_addr = models.URLField(max_length=300, unique=True)
    host_code = models.ForeignKey(Host, on_delete=models.CASCADE, blank=True)
    path_code = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return '{0}'.format(self.web_addr)
    def __unicode__(self):
        return '{0}'.format(self.web_addr)

    def save(self, *args, **kwargs):
        origin = urlparse(self.web_addr)
        host_addr = origin.scheme + '://' + origin.hostname
        self.host_code, _ = Host.objects.get_or_create(host_addr=host_addr)
        length = 7
        path_code = None
        while not path_code or Url.objects.filter(path_code=path_code).exists():
            path_code = get_random_string(length)
            length += 1
        self.path_code = path_code
        return super().save(*args, **kwargs)

    @property
    def shortcut(self):
        instance = self
        path = instance.host_code.addr_code + '-' + instance.path_code
        return path

from django.db import models


class Url(models.Model):
    origin_addr = models.CharField(max_length=300, unique=True)
    short_addr = models.URLField(max_length=300, unique=True)

    def __str__(self):
        return '{0}'.format(self.mac)
    def __unicode__(self):
        return '{0}'.format(self.mac)

    # def save(self, *args, **kwargs):
    #     self.short_addr = 
    #     return super().save(*args, **kwargs)

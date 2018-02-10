from django.db import models


class ZipInfo(models.Model):
    zipcode = models.CharField(max_length=20)
    response = models.TextField()

    def __unicode__(self):
        return self.zipcode

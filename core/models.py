from django.db import models


# Create your models here.
class MarketPlace(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='market_place_images/')

    def __str__(self):
        return "{}".format(self.name)


class ZipCode(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.code)


class Brand(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='brand_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    market_place = models.ForeignKey(MarketPlace, on_delete=models.CASCADE, null=True, blank=True)
    zip_code = models.ForeignKey(ZipCode, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class Channel(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField(upload_to='images/', null=True, blank=True)
    subject = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class Content(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    brands = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.SET_NULL, related_name='content_brand')
    marketplace = models.ForeignKey(MarketPlace, null=True, blank=True, on_delete=models.SET_NULL, related_name='content_marketplace')
    channel = models.ForeignKey(Channel, null=True, blank=True, on_delete=models.SET_NULL, related_name='content_channel')

    def __str__(self):
        return "{}".format(self.name)

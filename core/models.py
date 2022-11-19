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
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='brand_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    market_place = models.ForeignKey(MarketPlace, on_delete=models.CASCADE)
    zip_code = models.ForeignKey(ZipCode, on_delete=models.CASCADE)
    def __str__(self):
        return "{}".format(self.name)

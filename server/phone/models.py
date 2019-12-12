from django.db import models

class BrandName(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class ModelNumber(models.Model):
    brandID = models.ForeignKey(BrandName, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    modelImage = models.ImageField(upload_to='media/', default=None, blank=True)

    def __str__(self):
        return self.name

class Variant(models.Model):
    modelNumberId = models.ForeignKey(ModelNumber, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name
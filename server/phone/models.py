from django.db import models

class BrandName(models.Model):
    name = models.CharField(max_length=500)
    brandIcon = models.ImageField(upload_to='brand-icons/', default=None, blank=True)

    def __str__(self):
        return self.name

class ModelNumber(models.Model):
    brandID = models.ForeignKey(BrandName, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    modelImage = models.ImageField(upload_to='model-image/', default=None, blank=True)

    def __str__(self):
        return self.name

class Variant(models.Model):
    modelNumberId = models.ForeignKey(ModelNumber, on_delete=models.CASCADE)
    ram = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    no_issue_price = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    hasCharger = models.IntegerField(blank=True, null=True)
    hasBox = models.IntegerField(blank=True, null=True)
    hasHeadPhone = models.IntegerField(blank=True, null=True)
    billBelowThreeMonth = models.IntegerField(blank=True, null=True)
    billAboveThreeMonth = models.IntegerField(blank=True, null=True)
    isNew = models.IntegerField(blank=True, null=True)
    isExcellent = models.IntegerField(blank=True, null=True)
    isFair = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.modelNumberId.name +" "+ self.ram +" "+ self.storage
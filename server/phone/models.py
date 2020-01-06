from django.db import models

class BrandName(models.Model):
    name = models.CharField(max_length=500)
    brandIcon = models.ImageField(upload_to='brand-icons/', default=None, blank=True)

    class Meta:
        db_table = "BrandName"

    def __str__(self):
        return self.name

class ModelNumber(models.Model):
    brandID = models.ForeignKey(BrandName, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    modelImage = models.ImageField(upload_to='model-image/', default=None, blank=True)

    class Meta:
        db_table = "ModelNumber"

    def __str__(self):
        return self.name

class Variant(models.Model):
    modelNumberId = models.ForeignKey(ModelNumber, on_delete=models.CASCADE)
    ram = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)
    price = models.CharField(max_length=30, blank=True, null=True)
    no_issue_price = models.CharField(max_length=30, blank=True, null=True)
    hasCharger = models.CharField(max_length=30, blank=True, null=True)
    hasBox = models.CharField(max_length=30, blank=True, null=True)
    hasHeadPhone = models.CharField(max_length=30, blank=True, null=True)
    billBelowThreeMonth = models.CharField(max_length=30, blank=True, null=True)
    billAboveThreeMonth = models.CharField(max_length=30, blank=True, null=True)
    isNew = models.CharField(max_length=30, blank=True, null=True)
    isExcellent = models.CharField(max_length=30, blank=True, null=True)
    isFair = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = "Varient"

    def __str__(self):
        return self.modelNumberId.name +" "+ self.ram +" "+ self.storage
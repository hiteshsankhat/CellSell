from rest_framework import  serializers

from . import models

class BrandNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BrandName
        fields = "__all__"

class ModelNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelNumber
        fields = "__all__"

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Variant
        fields = "__all__"
    
class PhoneSerialiezer(serializers.ModelSerializer):
    class Meta:
        model = models.PhoneData
        fields = "__all__"
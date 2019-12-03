from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from . import models

class PhoneData(APIView):
    def get(self, request):
        variantsDb = models.Variant.objects.all()
        data = []
        for i in variantsDb:
            variantName = i.veriantName
            modelName = i.modelNumberId.modelName
            brandname = i.modelNumberId.brandID.name
            abc = models.PhoneData(brandName=brandname, variantname=variantName, modelName=modelName)
            data.append(serializers.PhoneSerialiezer(abc).data)

        return Response(data=data, status=200)
        
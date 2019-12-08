from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

from . import serializers
from . import models
from server import settings

content = settings.APPSETTINGS_DATA

def index(request):
    variantsDb = models.Variant.objects.all().order_by('modelNumberId')
    content['data'] = variantsDb

    print(dir(variantsDb[0].modelNumberId))
    return render(request, 'phone/index.html', content)
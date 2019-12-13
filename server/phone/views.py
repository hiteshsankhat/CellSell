from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render

from . import models
from server import settings
from .forms import ContactForm
from django.core.mail import send_mail


content = settings.APPSETTINGS_DATA
nametext = ""


def index(request):
    variantsDb = models.Variant.objects.all().order_by('modelNumberId')
    content['data'] = variantsDb
    return render(request, 'phone/index.html', content)

def getModels(request, brandID):
    try:
        modelNumberDB = models.ModelNumber.objects.filter(brandID_id=brandID)
        content['data'] = modelNumberDB
        content['type'] = "Model Number"
        if modelNumberDB :
            nametext = modelNumberDB[0].brandID.name
        else:
            nametext = None
        content['nametext'] = nametext
    except modelNumberDB.DoesNotExist:
        raise Http404("not found")
    return render(request, 'phone/index.html', content)


def getAllBrands(request):
    brandDB = models.BrandName.objects.all().order_by('name')
    content['data'] = brandDB
    content['type'] = "Brand"
    content['nametext'] = nametext
    return render(request, 'phone/index.html', content)

def getVarients(request, modelID):
    varientDB = models.Variant.objects.filter(modelNumberId_id=modelID).order_by('modelNumberId')
    content['data'] = varientDB
    content['type'] = "Varient"
    if varientDB:
        nametext = varientDB[0].modelNumberId.brandID.name + " " + varientDB[0].modelNumberId.name
        content['image'] = varientDB[0].modelNumberId.modelImage
    else:
        nametext = None
    content['nametext'] = nametext
    return render(request, 'phone/index.html', content)

def userContactForm(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = form.cleaned_data.get('message')
            send_mail("hello", msg, "kvirat2944@gmail.com", ["kvirat2944@gmail.com"])
            pass
    else:
        form = ContactForm()
    content['form'] = form
    return render(request, 'phone/form.html', content)

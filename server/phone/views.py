from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
import os
from . import models
from server import settings
from .forms import ContactForm
from django.core.mail import send_mail, EmailMessage
import json
from . import add_data, read_excel, write_excel, sendingMail
from django.core.files.storage import FileSystemStorage


content = settings.APPSETTINGS_DATA
nametext = ""


def index(request):
    add_data.insert()
    variantsDb = models.Variant.objects.all().order_by('modelNumberId')
    content['data'] = variantsDb
    return render(request, 'phone/index.html', content)


def notFound(request):
    return render(request, 'phone/404_page.html', content)


def thankYou(request):
    return render(request, 'phone/thank_you.html', content)


def getAllBrands(request):
    # add_data.insert();
    brandDB = models.BrandName.objects.all().order_by('name')
    content['data'] = brandDB
    content['type'] = "Brand"
    content['nametext'] = nametext
    return render(request, 'phone/brand_list.html', content)


def getModels(request, brandID):
    try:
        modelNumberDB = models.ModelNumber.objects.filter(brandID_id=brandID)
        content['data'] = modelNumberDB
        content['type'] = "Model Number"
    except modelNumberDB.DoesNotExist:
        raise Http404("not found")
    return render(request, 'phone/model_list.html', content)


def getVarients(request, modelID):
    varientDB = models.Variant.objects.filter(
        modelNumberId_id=modelID).order_by('modelNumberId')
    content['data'] = varientDB
    content['type'] = "Varient"
    if varientDB:
        nametext = varientDB[0].modelNumberId.name
        content['image'] = varientDB[0].modelNumberId.modelImage
    else:
        nametext = None
    content['nametext'] = nametext
    return render(request, 'phone/varient_list.html', content)


def phoneConditon(request, varientID):
    if request.method == "POST":
        request.session['data'] = request.POST
        return redirect('contact-form', varientID)
    if request.method == "GET":
        selected_phone = models.Variant.objects.get(pk=varientID)
        content['phoneData'] = selected_phone
        content['image'] = selected_phone.modelNumberId.modelImage
    return render(request, 'phone/phone_condition.html', content)


def userContactForm(request, varientID):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            selected_phone = models.Variant.objects.get(pk=varientID)
            data = request.session['data']
            sendingMail.sendMail(data, form, selected_phone);
            # subject, msg = preparedMailData(data, form, selected_phone)
            # msg = EmailMessage(subject=subject, body=msg, from_email="kvirat2944@gmail.com", to=[
            #                    "kvirat2944@gmail.com"])
            # msg.content_subtype = 'html'
            # msg.send()
            return redirect('thank-you-page')
    else:
        form = ContactForm()
    content['form'] = form
    return render(request, 'phone/form.html', content)


def autoComplete(request):
    data = {
        'data': 'fail'
    }
    if request.is_ajax():
        q = request.GET.get('search', '').capitalize()
        search_qs = models.ModelNumber.objects.filter(name__icontains=q)[:5]
        results = []
        for r in search_qs:
            results.append(r.name)
        data['data'] = results
    return JsonResponse(data)


def getSearchResult(request):
    data = {
        'data': 'fail'
    }
    if request.is_ajax():
        q = request.GET.get('search', '').capitalize()
        search_qs = models.ModelNumber.objects.filter(name__iexact=q)[:5]
        results = []
        for r in search_qs:
            results.append(r.pk)
        data['data'] = results
    return JsonResponse(data)


def importExcel(request):
    if request.method == 'POST' and request.FILES['excelFile']:
        file = request.FILES['excelFile']
        fs = FileSystemStorage()
        filename = fs.save("data.xlsx", file)
        path = os.path.join(settings.MEDIA_ROOT, filename)
        read_excel.insertALLData(path)
        fs.delete(filename)
        return JsonResponse({'success': 'true'})
    return JsonResponse({'success': 'false'})


def downloadExcel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="PhoneData.xls'
    return write_excel.export(response)
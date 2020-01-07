from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
import os
from . import models
from server import settings
from .forms import ContactForm
from django.core.mail import send_mail, EmailMessage
import json
from . import add_data, read_excel
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
            subject, msg = preparedMailData(data, form, selected_phone)
            msg = EmailMessage(subject=subject, body=msg, from_email="kvirat2944@gmail.com", to=[
                               "kvirat2944@gmail.com"])
            msg.content_subtype = 'html'
            msg.send()
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


def preparedMailData(data, form, phone):
    msg = '''
<table>
  <tr>
    <td>Name</td>
    <td>{name}</td>
  </tr>
  <tr>
    <td>Phone Number</td>
    <td>{phone}</td>
  </tr>
  <tr>
    <td colspan="2">Address</td>
  </tr>
  <tr>
    <td>Address line 1</td>
    <td>{add1}</td>
  </tr>
  <tr>
    <td>Address line 2</td>
    <td>{add2}</td>
  </tr>
  <tr>
    <td>City</td>
    <td>{city}</td>
  </tr>
  <tr>
    <td>State</td>
    <td>{state}</td>
  </tr>
  <tr>
    <td>Pin code</td>
    <td>{pinCode}</td>
  </tr>
  <tr>
    <td colspan="2">Phone Condition</td>
  </tr>
  <tr>
    <td>Issue</td>
    <td>{issue}</td>
  </tr>
  <tr>
    <td>Charger</td>
    <td>{charger}</td>
  </tr>
  <tr>
    <td>Ear Phone</td>
    <td>{earPhone}</td>
  </tr>
  <tr>
    <td>Box</td>
    <td>{box}</td>
  </tr>
  <tr>
    <td>Bill</td>
    <td>{bill}</td>
  </tr>
  <tr>
    <td>Condition</td>
    <td>{condition}</td>
  </tr>
</table>
        '''.format(
        name=form.cleaned_data.get("name"),
        add1=form.cleaned_data.get("addressLine1"),
        add2=form.cleaned_data.get("addressLine2"),
        city=form.cleaned_data.get("city"),
        state=form.cleaned_data.get("state"),
        pinCode=form.cleaned_data.get("pinCode"),
        phone=form.cleaned_data.get("phone"),
        issue=data.get("issue_no_issue"),
        charger=("Yes" if data.get("charger") else "NO"),
        earPhone=("Yes" if data.get("ear_phone") else "NO"),
        box=("Yes" if data.get("box") else "NO"),
        bill=data.get("valid_bill_status"),
        condition=data.get("phone_overall_condition")
    )

    name = phone.modelNumberId.name + " " + phone.ram + " " + phone.storage
    return (name, msg)


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

from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect

from . import models
from server import settings
from .forms import ContactForm
from django.core.mail import send_mail, EmailMessage
import json
from . import add_data


content = settings.APPSETTINGS_DATA
nametext = ""


def index(request):
    add_data.insert()
    variantsDb = models.Variant.objects.all().order_by('modelNumberId')
    content['data'] = variantsDb
    return render(request, 'phone/index.html', content)


def getModels(request, brandID):
    try:
        modelNumberDB = models.ModelNumber.objects.filter(brandID_id=brandID)
        content['data'] = modelNumberDB
        content['type'] = "Model Number"
    except modelNumberDB.DoesNotExist:
        raise Http404("not found")
    return render(request, 'phone/index.html', content)


def getAllBrands(request):
    # add_data.insert();
    brandDB = models.BrandName.objects.all().order_by('name')
    content['data'] = brandDB
    content['type'] = "Brand"
    content['nametext'] = nametext
    return render(request, 'phone/index.html', content)


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
    return render(request, 'phone/index.html', content)


def phoneConditon(request, varientID):
    if request.method == "POST":
        request.session['data'] = request.POST
        return redirect('contact-form', varientID)
    if request.method == "GET":
        selected_phone = models.Variant.objects.get(pk=varientID)
        content['phoneData'] = selected_phone
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
            pass
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
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<table class="tg">
  <tr>
    <th class="tg-0lax">Name</th>
    <th class="tg-0lax">{name}</th>
  </tr>
  <tr>
    <td class="tg-0lax" colspan="2">Address</td>
  </tr>
  <tr>
    <td class="tg-0lax">address line 1</td>
    <td class="tg-0lax">{add1}</td>
  </tr>
  <tr>
    <td class="tg-0lax">address line 2</td>
    <td class="tg-0lax">{add2}</td>
  </tr>
  <tr>
    <td class="tg-0lax">City</td>
    <td class="tg-0lax">{city}</td>
  </tr>
  <tr>
    <td class="tg-0lax">State</td>
    <td class="tg-0lax">{state}</td>
  </tr>
  <tr>
    <td class="tg-0lax">Pin code</td>
    <td class="tg-0lax">{pinCode}</td>
  </tr>
  <tr>
    <td class="tg-0lax">Phone</td>
    <td class="tg-0lax">{phone}</td>
  </tr>
  <tr>
    <td class="tg-0lax">Issue</td>
    <td class="tg-0lax">{issue}</td>
  </tr>
  <tr>
    <td class="tg-0lax">Charger</td>
    <td class="tg-0lax">{charger}</td>
  </tr>
  <tr>
    <td class="tg-0lax">Ear Phone</td>
    <td class="tg-0lax">{earPhone}</td>
  </tr>
  <tr>
    <td class="tg-0lax">Box</td>
    <td class="tg-0lax">{box}</td>
  </tr>
  <tr>
    <td class="tg-0lax">Bill</td>
    <td class="tg-0lax">{bill}</td>
  </tr>
  <tr>
    <td class="tg-0lax">Condition</td>
    <td class="tg-0lax">{condition}</td>
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

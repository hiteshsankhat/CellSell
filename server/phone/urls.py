from django.urls import path

from . import views
urlpatterns = [
    # path('get-phone-data', views.PhoneData.as_view())
    # path('', views.index),
    path('', views.getAllBrands, name="home"),
    path('modelnumber/<int:brandID>', views.getModels),
    path('varient/<int:modelID>', views.getVarients),
    path('phone-conditon/<int:varientID>', views.phoneConditon),
    path('contactform/<int:varientID>', views.userContactForm, name="contact-form"),
    path('autocomplete-search', views.autoComplete),
    path('get-search-result', views.getSearchResult),
    path('not-found-page', views.notFound),
    path('thank-you-page', views.thankYou, name="thank-you-page"),
    path('import-data-from-excel', views.importExcel, name="file-upload-page"),
    path('download-data', views.downloadExcel, name="download-excel")
]

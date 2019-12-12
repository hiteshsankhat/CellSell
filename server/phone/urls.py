from django.urls import path

from . import views
urlpatterns = [
    # path('get-phone-data', views.PhoneData.as_view())
    # path('', views.index),
    path('', views.getAllBrands),
    path('modelnumber/<int:brandID>', views.getModels),
    path('varient/<int:modelID>', views.getVarients),
    path('contactform/', views.userContactForm)
]

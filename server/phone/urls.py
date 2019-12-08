from django.urls import path

from . import views
urlpatterns = [
    # path('get-phone-data', views.PhoneData.as_view())
    path('', views.index)
]

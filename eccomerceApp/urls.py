from django.urls import path

from .views import Products, Products_details

urlpatterns = [
   path('', Products , name='Products') ,
   path('/<int:p_id>', Products_details , name='productDetails') 
]

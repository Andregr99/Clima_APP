from django.urls import path
from .views import buscar_clima, clima_api, index

urlpatterns = [
    path('buscar/<str:cidade>/', buscar_clima, name='buscar_clima'),
    path('api/clima/<str:cidade>/', clima_api, name='clima_api'),
    path('', index, name='index'),

]

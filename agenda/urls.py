from django.urls import path
from .views import (
    ProvinciaListarCriarView,
    ProvinciaRetrieveUpdateDeleteView,
    MunicipioListarCriarView,
    MunicipioRetrieveUpdateDeleteView,
    ContactoListarCriarView,
    ContactoRetrieveUpdateDeleteView,
)

urlpatterns = [
    path('provincias/', ProvinciaListarCriarView.as_view(), name='provincia-listar-criar'),
    path('provincias/<int:pk>/', ProvinciaRetrieveUpdateDeleteView.as_view(), name='provincia-detalhe'),

    path('municipios/', MunicipioListarCriarView.as_view(), name='municipio-listar-criar'),
    path('municipios/<int:pk>/', MunicipioRetrieveUpdateDeleteView.as_view(), name='municipio-detalhe'),

    path('contactos/', ContactoListarCriarView.as_view(), name='contacto-listar-criar'),
    path('contactos/<int:pk>/', ContactoRetrieveUpdateDeleteView.as_view(), name='contacto-detalhe'),
]

# agenda/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Provincia, Municipio, Contacto
from .serializers import ProvinciaSerializer, MunicipioSerializer, ContactoSerializer

class ProvinciaListarCriarView(generics.ListCreateAPIView):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer
    permission_classes = [IsAuthenticated]

class ProvinciaRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer
    permission_classes = [IsAuthenticated]


class MunicipioListarCriarView(generics.ListCreateAPIView):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
    permission_classes = [IsAuthenticated]

class MunicipioRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
    permission_classes = [IsAuthenticated]


class ContactoListarCriarView(generics.ListCreateAPIView):
    serializer_class = ContactoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Contacto.objects.filter(usuario=self.request.user).order_by('nome')

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class ContactoRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Contacto.objects.filter(usuario=self.request.user)

    def perform_update(self, serializer):
        serializer.save(usuario=self.request.user)  


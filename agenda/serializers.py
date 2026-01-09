from rest_framework import serializers
from .models import Provincia, Municipio, Contacto
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = ['id', 'nome']

class MunicipioSerializer(serializers.ModelSerializer):
    provincia = ProvinciaSerializer(read_only=True)  

    class Meta:
        model = Municipio
        fields = ['id', 'nome', 'provincia']

class ContactoSerializer(serializers.ModelSerializer):
    municipio = MunicipioSerializer(read_only=True)  
    municipio_id = serializers.PrimaryKeyRelatedField(
        queryset=Municipio.objects.all(),
        source='municipio',  
        write_only=True
    )

    class Meta:
        model = Contacto
        fields = ['id', 'nome', 'telefone', 'email', 'endereco', 'observacoes', 'municipio', 'municipio_id']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_id'] = self.user.id  
        return data
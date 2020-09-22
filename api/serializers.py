from rest_framework import serializers
from .models import Provider,Etf,Component,Price

# ***********Aca usaremos serializers, siginifica que haremos todo a mano***************
# class ProviderSerializer(serializers.Serializer):
#     '''Funcion para crear la transformacion de data a JSON'''
    
#     id_provider = serializers.CharField(max_length=100)
#     name_provider = serializers.CharField(max_length=100)
#     detail_provider = serializers.CharField(max_length=100)


#     def create(self,validated_data):
#         return Provider.objects.create(validated_data)


#     def update(self, instance, validated_data):
#         instance.id_provider = validated_data.get('id_provider',instance.id_provider)
#         instance.name_provider = validated_data.get('name_provider',instance.name_provider)
#         instance.detail_provider = validated_data.get('detail_provider',instance.detail_provider)
#         instance.save()
#         return instance
    
#     '''
#     *Codigo para rescatar la data del serializador 
#     from api.models import Provider
#     from api.serializers import ProviderSerializer
#     from rest_framework.renderers import JSONRenderer
#     from rest_framework.parsers import JSONParser
#     p = Provider(id_provider=1,name_provider="Proveedor 1",detail_provider="Detalle del proveedor 1")
#     p.save()
#     serializer = ProviderSerializer(p)
#     serializer.data()
#     serializer.data
#     content = JSONRenderer().render(serializer.data)
#     content
#     history
#     '''

#***********Aca usaremos el ModelSerializer, practicamente te hace la pega de arriba pero mas facil y rapida
class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        # fields = ['id_provider','name_provider','detail_provider']# tambien se puede dejar asi --> '__all__'
        fields = ('__all__')

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('__all__')


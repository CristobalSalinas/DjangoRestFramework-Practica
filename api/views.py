from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Provider,Price
from .serializers import ProviderSerializer,PriceSerializer
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

#De la manera principal
@csrf_exempt
def all_providers(request):
    '''Obtener informacion de todos los proveedores
    * GET = Obtener todos los proveedores
    * POST = Añadir proveedores, 1 o mas de 1 '''

    if request.method == 'GET':
        # return JsonResponse({"status_get":"ok"})
        providers = Provider.objects.all()
        serializer = ProviderSerializer(providers,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProviderSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)



@csrf_exempt
def specific_provider(request,pk):
    '''Metodo para provider en especifico desde id
    *GET= Obtengo el provider especifico
    *PUT= Edito el proveedor con la data que paso
    *POST= Añado un proveedor con la data que paso
    *DELETE= se elimina el proveedor con el id que le pasamos'''

    try:
        provider = Provider.objects.get(pk=pk)
    except Provider.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProviderSerializer(provider)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProviderSerializer(provider,data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProviderSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)
    elif request.method == 'DELETE':
        provider.delete()
        return HttpResponse(status=201)


#con api view, este me muestra una pantalla con la data mas especifica y bonita
@api_view(['GET','POST'])
def all_prices(request):

    if request.method == 'GET':
        prices = Price.objects.all()
        serializer = PriceSerializer(prices,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PriceSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
        

@api_view(['GET','POST','PUT','DELETE'])
def specific_price(request,pk):

    try:
        price = Price.objects.get(pk=pk)
    except Price.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PriceSerializer(price)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PriceSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'PUT':
        serializer = PriceSerializer(price,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE':
        price.delete()
        return HttpResponse(status=201)


#De manera que sea una clase, asi es mas facil
#Lo voy a volver hacer con providers, ya que es mas corto
class ProvidersAPIView(APIView):
    def get(self,request):
        providers = Provider.objects.all()
        serializer = ProviderSerializer(providers,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ProviderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 



class SpecificProviderAPIView(APIView):

    def get_object(self,id):
        try:
            return Provider.objects.get(pk=id)
        except Provider.DoesNotExist:
            return HttpResponse(status=404)


    def get(self,request,pk):
        provider = self.get_object(pk)
        serializer = ProviderSerializer(provider)
        return Response(serializer.data)


    def post(self,request,pk):
        serializer = ProviderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 


    def put(self,request,pk):
        provider = self.get_object(pk)
        serializer = ProviderSerializer(provider,request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 


    def delete(self,request,pk):
        providers = self.get_object(pk)
        providers.delete()
        return HttpResponse(status=201)


##############################################################################

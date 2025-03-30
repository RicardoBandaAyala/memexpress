from django.shortcuts import render
from shopapp.models import Product
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
def get_all_products(request):
    queryset = Product.objects.all()
    res = serializers.serialize('json', queryset)
    #return JsonResponse(list(queryset.values()), safe=False)
    return JsonResponse(res, safe=False) 
#como el sistema esta serializando objetos "como dios le dio a entender", per con el seguro de que es un json, se pone safe=False
#para que no haya problemas con la serializacion

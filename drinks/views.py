from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .serializers import DrinkSerializer
from .models import Drink
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def drink_list(request):

	if request.method == "GET":
		drinks =  Drink.objects.all()
		serializer  = DrinkSerializer(drinks, many=True)
		return JsonResponse({"drinks": serializer.data}, safe=False)

	if request.method == "POST":
		serializer = DrinkSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)







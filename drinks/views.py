from django.shortcuts import request,render,HttpResponse
from django.http import JsonResponse
from .serializers import DrinkSerializer
from .models import Drink


def drink_list(request):
	drinks =  Drink.objects.all()
	return render(request, template_name)
from django.shortcuts import render
from django.http import HttpResponse
from .models import Preguntas, Respuestas
# Create your views here.


def home(request,mensaje):

	saludo = Preguntas.objects.all()
	
	return HttpResponse( saludo)



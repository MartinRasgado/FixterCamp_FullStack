from django.shortcuts import render, HttpResponse
from django.views.generic import View


class Sabado(View):
	def get(self,request):
		#return HttpResponse('Funciono la app')
		return render(request,'hola.html')

#class Domingo(View):
#	def get(self,request):
#		return HttpResponse('Funciono la app')

from django.http import HttpResponse, JsonResponse
from django.template import loader
from ..BL.CitiesBL import CitiesBL as ctbl
from ..Models import *
import json
class CityController:
	def allCities(self,request):
		acto = ctbl.allCities();
		return HttpResponse(Common.Common().ConverttoJson(acto), content_type="application/json")

	def addCity(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			ucto = City.City();
			ucto.country_id = ud['countryid']
			ucto.fullName = ud['name']
			ucto.PhoneCode = ud['phonecode']
			ucto.PostalCode = ud['postalcode']
			ucto.isActive = ud['active']
		return HttpResponse(Common.Common().ConverttoJson(ctbl.addCity(ucto)), content_type="application/json")

	def selectCity(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			ucto = City.City();
			ucto.Id = ud['id']
		return HttpResponse(Common.Common().ConverttoJson(ctbl.selectCity(ucto)), content_type="application/json")

	def updateCity(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			ucto = City.City();
			ucto.Id = ud['id']
			ucto.country_id = ud['countryid']
			ucto.fullName = ud['name']
			ucto.PhoneCode = ud['phonecode']
			ucto.PostalCode = ud['postalcode']
			ucto.isActive = ud['active']
		return HttpResponse(Common.Common().ConverttoJson(ctbl.updateCity(ucto)), content_type="application/json")

	def deleteCity(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			ucto = City.City();
			ucto.Id = ud['id']
		return HttpResponse(Common.Common().ConverttoJson(ctbl.deleteCity(ucto)), content_type="application/json")		
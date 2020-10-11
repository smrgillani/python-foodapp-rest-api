from django.http import HttpResponse, JsonResponse
from django.template import loader
from ..BL.CountriesBL import CountriesBL as ctbl
from ..Models import *
import json
class CountryController:
	def allCountries(self,request):
		acto = ctbl.allCountries();
		return HttpResponse(Common.Common().ConverttoJson(acto), content_type="application/json")

	def addCountry(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			ucto = Country.Country();
			ucto.currency_id = ud['currencyid']
			ucto.fullName = ud['name']
			ucto.ISO = ud['iso']
			ucto.PhoneCode = ud['phonecode']
			ucto.isActive = ud['active']
		return HttpResponse(Common.Common().ConverttoJson(ctbl.addCountry(ucto)), content_type="application/json")

	def selectCountry(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			ucto = Country.Country();
			ucto.Id = ud['id']
		return HttpResponse(Common.Common().ConverttoJson(ctbl.selectCountry(ucto)), content_type="application/json")

	def updateCountry(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			ucto = Country.Country();
			ucto.Id = ud['id']
			ucto.currency_id = ud['currencyid']
			ucto.fullName = ud['name']
			ucto.ISO = ud['iso']
			ucto.PhoneCode = ud['phonecode']
			ucto.isActive = ud['active']
		return HttpResponse(Common.Common().ConverttoJson(ctbl.updateCountry(ucto)), content_type="application/json")

	def deleteCountry(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			ucto = Country.Country();
			ucto.Id = ud['id']
		return HttpResponse(Common.Common().ConverttoJson(ctbl.deleteCountry(ucto)), content_type="application/json")		
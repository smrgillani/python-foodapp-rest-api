from django.http import HttpResponse, JsonResponse
from django.template import loader
from ..BL.CurrenciesBL import CurrenciesBL as ccbl
from ..Models import *
import json
class CurrencyController:
	def allCurrencies(self,request):
		acco = ccbl.allCurrencies();
		return HttpResponse(Common.Common().ConverttoJson(acco), content_type="application/json")

	def addCurrency(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			ucco = Currency.Currency();
			ucco.fullName = ud['name']
			ucco.Sign = ud['sign']
			ucco.isActive = ud['active']
		return HttpResponse(Common.Common().ConverttoJson(ccbl.addCurrency(ucco)), content_type="application/json")

	def selectCurrency(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			ucco = Currency.Currency();
			ucco.Id = ud['id']
		return HttpResponse(Common.Common().ConverttoJson(ccbl.selectCurrency(ucco)), content_type="application/json")

	def updateCurrency(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			ucco = ContactType.ContactType();
			ucco.Id = ud['id']
			ucco.fullName = ud['name']
			ucco.Sign = ud['sign']
			ucco.isActive = ud['active']
		return HttpResponse(Common.Common().ConverttoJson(ccbl.updateCurrency(ucco)), content_type="application/json")

	def deleteCurrency(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			ucco = Currency.Currency();
			ucco.Id = ud['id']
		return HttpResponse(Common.Common().ConverttoJson(ccbl.deleteCurrency(ucco)), content_type="application/json")		
from django.http import HttpResponse, JsonResponse
from django.template import loader
from ..BL.LocalAddressesBL import LocalAddressesBL as labl
from ..Models import *
import json
class LocalAddressController:
	def allLocalAddresses(self,request):
		alao = labl.allLocalAddresses();
		return HttpResponse(Common.Common().ConverttoJson(alao), content_type="application/json")

	def addLocalAddress(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			ulao = LocalAddress.LocalAddress();
			ulao.city_id = ud['cityid']
			ulao.fullAddress = ud['fulladdress']
			ulao.isActive = ud['active']
		return HttpResponse(Common.Common().ConverttoJson(labl.addLocalAddress(ulao)), content_type="application/json")

	def selectLocalAddress(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			ulao = LocalAddress.LocalAddress();
			ulao.Id = ud['id']
		return HttpResponse(Common.Common().ConverttoJson(labl.selectLocalAddress(ulao)), content_type="application/json")

	def updateLocalAddress(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			ulao = LocalAddress.LocalAddress();
			ulao.Id = ud['id']
			ulao.city_id = ud['cityid']
			ulao.fullAddress = ud['fulladdress']
			ulao.isActive = ud['active']
		return HttpResponse(Common.Common().ConverttoJson(labl.updateLocalAddress(ulao)), content_type="application/json")

	def deleteLocalAddress(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			ulao = LocalAddress.LocalAddress();
			ulao.Id = ud['id']
		return HttpResponse(Common.Common().ConverttoJson(labl.deleteLocalAddress(ulao)), content_type="application/json")		
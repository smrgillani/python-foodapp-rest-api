from django.http import HttpResponse, JsonResponse
from django.template import loader
from ..BL.ContactTypesBL import ContactTypesBL as ctbl
from ..Models import *
import json
class ContactTypeController:
	def allContactTypes(self,request):
		acto = ctbl.allContactTypes();
		return HttpResponse(Common.Common().ConverttoJson(acto), content_type="application/json")

	def addContactType(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			ucto = ContactType.ContactType();
			ucto.FullName = ud['name']
			ucto.isActive = ud['active']
		return HttpResponse(Common.Common().ConverttoJson(ctbl.addContactType(ucto)), content_type="application/json")

	def selectContactType(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			ucto = ContactType.ContactType();
			ucto.Id = ud['id']
		return HttpResponse(Common.Common().ConverttoJson(ctbl.selectContactType(ucto)), content_type="application/json")

	def updateContactType(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			ucto = ContactType.ContactType();
			ucto.Id = ud['id']
			ucto.FullName = ud['name']
			ucto.isActive = ud['active']
		return HttpResponse(Common.Common().ConverttoJson(ctbl.updateContactType(ucto)), content_type="application/json")

	def deleteContactType(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			ucto = ContactType.ContactType();
			ucto.Id = ud['id']
		return HttpResponse(Common.Common().ConverttoJson(ctbl.deleteContactType(ucto)), content_type="application/json")
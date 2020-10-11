from django.http import HttpResponse, JsonResponse
from django.template import loader
from ..BL.UserPermissionsBL import UserPermissionsBL as upbl
from ..Models import *
import json
class UserPermissionController:
	def allUserPermissions(self,request):
		aupo = upbl.allUserPermissions();
		return HttpResponse(Common.Common().ConverttoJson(aupo), content_type="application/json")

	def addUserPermission(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			uupo = UserPermission.UserPermission();
			uupo.userRole_id = ud['userroleid']
			uupo.systemPermission_id = ud['systempermissionid']
			uupo.isActive = ud['active']
		return HttpResponse(Common.Common().ConverttoJson(upbl.addUserPermission(uupo)), content_type="application/json")

	def selectUserPermission(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			uupo = UserPermission.UserPermission();
			uupo.Id = ud['id']
		return HttpResponse(Common.Common().ConverttoJson(upbl.selectUserPermission(uupo)), content_type="application/json")

	def updateUserPermission(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			uupo = UserPermission.UserPermission();
			uupo.Id = ud['id']
			uupo.userRole_id = ud['userroleid']
			uupo.systemPermission_id = ud['systempermissionid']
			uupo.isActive = ud['active']
		return HttpResponse(Common.Common().ConverttoJson(upbl.updateUserPermission(uupo)), content_type="application/json")

	def deleteUserPermission(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			uupo = UserPermission.UserPermission();
			uupo.Id = ud['id']
		return HttpResponse(Common.Common().ConverttoJson(upbl.deleteUserPermission(uupo)), content_type="application/json")		
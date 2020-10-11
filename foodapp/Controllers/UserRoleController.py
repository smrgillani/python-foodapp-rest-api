from django.http import HttpResponse, JsonResponse
from django.template import loader
from ..BL.UserRolesBL import UserRolesBL as urbl
from ..Models import *
import json
class UserRoleController:
	def allUserRoles(self,request):
		auro = urbl.allUserRoles();
		return HttpResponse(Common.Common().ConverttoJson(auro), content_type="application/json")

	def addUserRole(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			uuro = UserRole.UserRole();
			uuro.fullName = ud['fullname']
			uuro.isActive = ud['active']
		return HttpResponse(Common.Common().ConverttoJson(urbl.addUserRole(uuro)), content_type="application/json")

	def selectUserRole(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			uuro = UserRole.UserRole();
			uuro.Id = ud['id']
		return HttpResponse(Common.Common().ConverttoJson(urbl.selectUserRole(uuro)), content_type="application/json")

	def updateUserRole(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			uuro = UserRole.UserRole();
			uuro.Id = ud['id']
			uuro.fullName = ud['fullname']
			uuro.isActive = ud['active']
		return HttpResponse(Common.Common().ConverttoJson(urbl.updateUserRole(uuro)), content_type="application/json")

	def deleteUserRole(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			uuro = UserRole.UserRole();
			uuro.Id = ud['id']
		return HttpResponse(Common.Common().ConverttoJson(urbl.deleteUserRole(uuro)), content_type="application/json")		
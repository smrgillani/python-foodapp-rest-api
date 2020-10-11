from django.http import HttpResponse, JsonResponse
from django.template import loader
from ..BL.SystemPermissionsBL import SystemPermissionsBL as spbl
from ..Models import *
import json
class SystemPermissionController:
	def allSystemPermissions(self,request):
		aspo = spbl.allSystemPermissions();
		return HttpResponse(Common.Common().ConverttoJson(aspo), content_type="application/json")

	def addSystemPermission(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			uspo = SystemPermission.SystemPermission();
			uspo.moduleName = ud['modulename']
			uspo.permissionName = ud['permissionname']
			uspo.isActive = ud['active']
		return HttpResponse(Common.Common().ConverttoJson(spbl.addSystemPermission(uspo)), content_type="application/json")

	def selectSystemPermission(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			uspo = SystemPermission.SystemPermission();
			uspo.Id = ud['id']
		return HttpResponse(Common.Common().ConverttoJson(spbl.selectSystemPermission(uspo)), content_type="application/json")

	def updateSystemPermission(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			uspo = SystemPermission.SystemPermission();
			uspo.Id = ud['id']
			uspo.moduleName = ud['modulename']
			uspo.permissionName = ud['permissionname']
			uspo.isActive = ud['active']
		return HttpResponse(Common.Common().ConverttoJson(spbl.updateSystemPermission(uspo)), content_type="application/json")

	def deleteSystemPermission(self,request):
		if request.method == 'POST':
			ud = json.loads(request.body)
			uspo = SystemPermission.SystemPermission();
			uspo.Id = ud['id']
		return HttpResponse(Common.Common().ConverttoJson(spbl.deleteSystemPermission(uspo)), content_type="application/json")		
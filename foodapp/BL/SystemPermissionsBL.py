from ..DAL.SystemPermissionsDAL import SystemPermissionsDAL as sp
from ..Models.SystemPermission import SystemPermission

class SystemPermissionsBL():

	def allSystemPermissions():
		asp = sp.allSystemPermissions()
		SystemPermissions = list()
		for i in asp:
			SystmPrmsn = SystemPermission()
			SystmPrmsn.Id = i.id
			SystmPrmsn.permissionName = i.permissionName
			SystmPrmsn.moduleName = i.moduleName
			SystmPrmsn.isActive = i.isActive
			SystemPermissions.append(SystmPrmsn)
		return SystemPermissions

	def addSystemPermission(ico):
		rspo = sp.addSystemPermission(ico)
		SystmPrmsn = SystemPermission();
		SystmPrmsn.Id = rspo.id
		SystmPrmsn.permissionName = rspo.permissionName
		SystmPrmsn.moduleName = rspo.moduleName
		SystmPrmsn.isActive = rspo.isActive
		return SystmPrmsn

	def selectSystemPermission(ico):
		rspo = sp.selectOneSystemPermission(ico)
		SystmPrmsn = SystemPermission();
		SystmPrmsn.Id = rspo.id
		SystmPrmsn.permissionName = rspo.permissionName
		SystmPrmsn.moduleName = rspo.moduleName
		SystmPrmsn.isActive = rspo.isActive
		return SystmPrmsn

	def updateSystemPermission(ico):
		rspo = sp.updateSystemPermission(ico)
		SystmPrmsn = SystemPermission();
		SystmPrmsn.Id = rspo.id
		SystmPrmsn.permissionName = rspo.permissionName
		SystmPrmsn.moduleName = rspo.moduleName
		SystmPrmsn.isActive = rspo.isActive
		return SystmPrmsn

	def deleteSystemPermission(ico):
		rspo = sp.deleteSystemPermission(ico)
		return rspo
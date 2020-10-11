from ..Entities.SystemPermissions import SystemPermissions as sp
import datetime

class SystemPermissionsDAL:
	def allSystemPermissions():
		return sp.objects.all()
	def addSystemPermission(ico):
		return sp.objects.create(permissionName=ico.permissionName, moduleName=ico.moduleName, isActive=ico.isActive, created_at=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f"))
	def selectOneSystemPermission(ico):
		return sp.objects.get(id=ico.Id)
	def updateSystemPermission(ico):
		qrr = sp.objects.filter(id=ico.Id).update(permissionName=ico.permissionName, moduleName=ico.moduleName, isActive=ico.isActive, updated_at=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f"))
		return (None, sp.objects.get(id=ico.Id)) [qrr != 0]
	def deleteSystemPermission(ico):
		qrr = sp.objects.filter(id=ico.Id).delete()
		return (False, True) [qrr[0] != 0]
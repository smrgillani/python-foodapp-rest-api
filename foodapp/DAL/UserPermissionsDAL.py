from ..Entities.UserPermissions import UserPermissions as up
import datetime

class UserPermissionsDAL:
	def allUserPermissions():
		return up.objects.all()
	def addUserPermission(ico):
		return up.objects.create(userRole_id=ico.userRole_id, systemPermission_id=ico.systemPermission_id, isActive=ico.isActive, created_at=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f"))
	def selectOneUserPermission(ico):
		return up.objects.get(id=ico.Id)
	def updateUserPermission(ico):
		qrr = up.objects.filter(id=ico.Id).update(userRole_id=ico.userRole_id, systemPermission_id=ico.systemPermission_id, isActive=ico.isActive, updated_at=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f"))
		return (None, up.objects.get(id=ico.Id)) [qrr != 0]
	def deleteUserPermission(ico):
		qrr = up.objects.filter(id=ico.Id).delete()
		return (False, True) [qrr[0] != 0]
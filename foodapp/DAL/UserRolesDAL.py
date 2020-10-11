from ..Entities.UserRoles import UserRoles as ur
import datetime

class UserRolesDAL:
	def allUserRoles():
		return ur.objects.all()
	def addUserRole(ico):
		return ur.objects.create(fullName=ico.fullName, isActive=ico.isActive, created_at=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f"))
	def selectOneUserRole(ico):
		return ur.objects.get(id=ico.Id)
	def updateUserRole(ico):
		qrr = ur.objects.filter(id=ico.Id).update(fullName=ico.fullName, isActive=ico.isActive, updated_at=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f"))
		return (None, ur.objects.get(id=ico.Id)) [qrr != 0]
	def deleteUserRole(ico):
		qrr = ur.objects.filter(id=ico.Id).delete()
		return (False, True) [qrr[0] != 0]
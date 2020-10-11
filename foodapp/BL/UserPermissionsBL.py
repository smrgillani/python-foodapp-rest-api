from ..DAL.UserPermissionsDAL import UserPermissionsDAL as up
from ..Models.UserPermission import UserPermission

class UserPermissionsBL():

	def allUserPermissions():
		aup = up.allUserPermissions()
		UserPermissions = list()
		for i in aup:
			UsrPrmsn = UserPermission()
			UsrPrmsn.Id = i.id
			UsrPrmsn.userRole_id = i.userRole_id
			UsrPrmsn.systemPermission_id = i.systemPermission_id
			UsrPrmsn.isActive = i.isActive
			UserPermissions.append(UsrPrmsn)
		return UserPermissions

	def addUserPermission(ico):
		rupo = up.addUserPermission(ico)
		UsrPrmsn = UserPermission();
		UsrPrmsn.Id = rupo.id
		UsrPrmsn.userRole_id = rupo.userRole_id
		UsrPrmsn.systemPermission_id = rupo.systemPermission_id
		UsrPrmsn.isActive = rupo.isActive
		return UsrPrmsn

	def selectUserPermission(ico):
		rupo = up.selectOneUserPermission(ico)
		UsrPrmsn = UserPermission();
		UsrPrmsn.Id = rupo.id
		UsrPrmsn.userRole_id = rupo.userRole_id
		UsrPrmsn.systemPermission_id = rupo.systemPermission_id
		UsrPrmsn.isActive = rupo.isActive
		return UsrPrmsn

	def updateUserPermission(ico):
		rupo = up.updateUserPermission(ico)
		UsrPrmsn = UserPermission();
		UsrPrmsn.Id = rupo.id
		UsrPrmsn.userRole_id = rupo.userRole_id
		UsrPrmsn.systemPermission_id = rupo.systemPermission_id
		UsrPrmsn.isActive = rupo.isActive
		return UsrPrmsn

	def deleteUserPermission(ico):
		rupo = up.deleteUserPermission(ico)
		return rupo
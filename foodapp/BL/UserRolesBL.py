from ..DAL.UserRolesDAL import UserRolesDAL as ur
from ..Models.UserRole import UserRole

class UserRolesBL():

	def allUserRoles():
		aur = ur.allUserRoles()
		UserRoles = list()
		for i in aur:
			UsrRl = UserRole()
			UsrRl.Id = i.id
			UsrRl.fullName = i.fullName
			UsrRl.isActive = i.isActive
			UserRoles.append(UsrRl)
		return UserRoles

	def addUserRole(ico):
		ruro = ur.addUserRole(ico)
		UsrRl = UserRole();
		UsrRl.Id = ruro.id
		UsrRl.fullName = ruro.fullName
		UsrRl.isActive = ruro.isActive
		return UsrRl

	def selectUserRole(ico):
		ruro = ur.selectOneUserRole(ico)
		UsrRl = UserRole();
		UsrRl.Id = ruro.id
		UsrRl.fullName = ruro.fullName
		UsrRl.isActive = ruro.isActive
		return UsrRl

	def updateUserRole(ico):
		ruro = ur.updateUserRole(ico)
		UsrRl = UserRole();
		UsrRl.Id = ruro.id
		UsrRl.fullName = ruro.fullName
		UsrRl.isActive = ruro.isActive
		return UsrRl

	def deleteUserRole(ico):
		ruro = ur.deleteUserRole(ico)
		return ruro
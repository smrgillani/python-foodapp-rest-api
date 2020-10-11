from ..DAL.ContactTypesDAL import ContactTypesDAL as ct
from ..Models.ContactType import ContactType

class ContactTypesBL():

	def allContactTypes():
		act = ct.allContactTypes()
		ContactTypes = list()
		for i in act:
			cntctType = ContactType()
			cntctType.Id = i.id
			cntctType.FullName = i.FullName
			cntctType.isActive = i.isActive
			ContactTypes.append(cntctType)
		return ContactTypes

	def addContactType(ico):
		rcto = ct.addContactType(ico)
		cntctType = ContactType();
		cntctType.Id = rcto.id
		cntctType.FullName = rcto.FullName
		cntctType.isActive = rcto.isActive
		cntctType.created_at = rcto.created_at
		return cntctType

	def selectContactType(ico):
		rcto = ct.selectOneContactType(ico)
		cntctType = ContactType();
		cntctType.Id = rcto.id
		cntctType.FullName = rcto.FullName
		cntctType.isActive = rcto.isActive
		return cntctType

	def updateContactType(ico):
		rcto = ct.updateContactType(ico)
		cntctType = ContactType();
		cntctType.Id = rcto.id
		cntctType.FullName = rcto.FullName
		cntctType.isActive = rcto.isActive
		cntctType.updated_at = rcto.updated_at
		return cntctType

	def deleteContactType(ico):
		rcto = ct.deleteContactType(ico)
		return rcto
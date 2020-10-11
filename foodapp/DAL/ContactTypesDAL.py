from ..Entities.ContactTypes import ContactTypes as ct
import datetime

class ContactTypesDAL:
	def allContactTypes():
		return ct.objects.all()
	def addContactType(ico):
		return ct.objects.create(FullName=ico.FullName, isActive=ico.isActive, created_at=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f"))
	def selectOneContactType(ico):
		return ct.objects.get(id=ico.Id)
	def updateContactType(ico):
		qrr = ct.objects.filter(id=ico.Id).update(FullName=ico.FullName, isActive=ico.isActive, updated_at=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f"))
		return (None, ct.objects.get(id=ico.Id)) [qrr != 0]
	def deleteContactType(ico):
		qrr = ct.objects.filter(id=ico.Id).delete()
		return (False, True) [qrr[0] != 0]
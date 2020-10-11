from ..Entities.LocalAddresses import LocalAddresses as la
import datetime

class LocalAddressesDAL:
	def allLocalAddresses():
		return la.objects.all()
	def addLocalAddress(ico):
		return la.objects.create(city_id=ico.city_id, fullAddress=ico.fullAddress, isActive=ico.isActive, created_at=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f"))
	def selectOneLocalAddress(ico):
		return la.objects.get(id=ico.Id)
	def updateLocalAddress(ico):
		qrr = la.objects.filter(id=ico.Id).update(city_id=ico.city_id, fullAddress=ico.fullAddress, isActive=ico.isActive, updated_at=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f"))
		return (None, la.objects.get(id=ico.Id)) [qrr != 0]
	def deleteLocalAddress(ico):
		qrr = la.objects.filter(id=ico.Id).delete()
		return (False, True) [qrr[0] != 0]
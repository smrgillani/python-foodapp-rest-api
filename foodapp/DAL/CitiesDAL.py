from ..Entities.Cities import Cities as ct
import datetime

class CitiesDAL:
	def allCities():
		return ct.objects.all()
	def addCity(ico):
		return ct.objects.create(country_id=ico.country_id, fullName=ico.fullName, PhoneCode=ico.PhoneCode, PostalCode=ico.PostalCode, isActive=ico.isActive, created_at=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f"))
	def selectOneCity(ico):
		return ct.objects.get(id=ico.Id)
	def updateCity(ico):
		qrr = ct.objects.filter(id=ico.Id).update(country_id=ico.country_id, fullName=ico.fullName, PhoneCode=ico.PhoneCode, PostalCode=ico.PostalCode, isActive=ico.isActive, updated_at=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f"))
		return (None, ct.objects.get(id=ico.Id)) [qrr != 0]
	def deleteCity(ico):
		qrr = ct.objects.filter(id=ico.Id).delete()
		return (False, True) [qrr[0] != 0]
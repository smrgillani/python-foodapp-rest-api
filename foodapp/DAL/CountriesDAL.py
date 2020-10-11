from ..Entities.Countries import Countries as ct
import datetime

class CountriesDAL:
	def allCountries():
		return ct.objects.all()
	def addCountry(ico):
		return ct.objects.create(currency_id=ico.currency_id, fullName=ico.fullName, ISO=ico.ISO, PhoneCode=ico.PhoneCode, isActive=ico.isActive, created_at=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f"))
	def selectOneCountry(ico):
		return ct.objects.get(id=ico.Id)
	def updateCountry(ico):
		qrr = ct.objects.filter(id=ico.Id).update(currency_id=ico.currency_id, fullName=ico.fullName, ISO=ico.ISO, PhoneCode=ico.PhoneCode, isActive=ico.isActive, updated_at=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f"))
		return (None, ct.objects.get(id=ico.Id)) [qrr != 0]
	def deleteCountry(ico):
		qrr = ct.objects.filter(id=ico.Id).delete()
		return (False, True) [qrr[0] != 0]